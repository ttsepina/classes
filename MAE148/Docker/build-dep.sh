#!/usr/bin/env bash

#Setup/Vars

readonly PREFIX=/usr/local
readonly DEF_VERSION=4.9.0
readonly CPUS = $(nproc)
readonly ARCH=$(uname -i)

# better board detection. if it has 6 or more cpus, it probably has a ton of ram too
if [[ $CPUS -gt 5 ]]; then
    # something with a ton of ram
    JOBS=$CPUS
else
    JOBS=2  # you can set this to 4 if you have a swap file
    # otherwise a Nano will choke towards the end of the build
fi

#Function Definitions

#Places WD in /tmp/build_opencv and 
setup () {
    cd /tmp
    if [[ -d "build_opencv" ]] ; then
        echo "It appears an existing build exists in /tmp/build_opencv"
        echo "Clear build_opencv if you want to install a new version"
    else
        mkdir build_opencv
        cd build_opencv
    fi
}

git_source () {
    echo "Getting version '$1' of OpenCV"
    git clone --depth 1 --branch "$1" https://github.com/opencv/opencv.git
    git clone --depth 1 --branch "$1" https://github.com/opencv/opencv_contrib.git
}

configure () {
    local CMAKEFLAGS="
        -D CPACK_BINARY_DEB=ON \
        -D BUILD_EXAMPLES=OFF \
        -D BUILD_opencv_python2=OFF \
        -D BUILD_opencv_python3=ON \
        -D BUILD_opencv_java=OFF \
        -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D CUDA_ARCH_BIN=${CUDA_ARCH_BIN} \
        -D CUDA_ARCH_PTX= \
        -D CUDA_FAST_MATH=ON \
        -D CUDNN_INCLUDE_DIR=/usr/include/$(uname -i)-linux-gnu \
        -D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
        -D WITH_EIGEN=ON \
        -D ENABLE_NEON=ON \
        -D OPENCV_DNN_CUDA=ON \
        -D OPENCV_ENABLE_NONFREE=ON \
        -D OPENCV_EXTRA_MODULES_PATH=/opt/opencv-python/opencv_contrib/modules \
        -D OPENCV_GENERATE_PKGCONFIG=ON \
        -D OpenGL_GL_PREFERENCE=GLVND \
        -D WITH_CUBLAS=ON \
        -D WITH_CUDA=ON \
        -D WITH_CUDNN=ON \
        -D WITH_GSTREAMER=ON \
        -D WITH_LIBV4L=ON \
        -D WITH_GTK=ON \
        -D WITH_OPENGL=OFF \
        -D WITH_OPENCL=OFF \
        -D WITH_IPP=OFF \
        -D WITH_TBB=ON \
        -D BUILD_TIFF=ON \
        -D BUILD_PERF_TESTS=OFF \
        -D BUILD_TESTS=OFF"

    if [[ "$1" != "test" ]] ; then
        CMAKEFLAGS="
        ${CMAKEFLAGS}
        -D BUILD_PERF_TESTS=OFF
        -D BUILD_TESTS=OFF"
    fi

    echo "cmake flags: ${CMAKEFLAGS}"

    cd opencv
    mkdir build
    cd build
    cmake ${CMAKEFLAGS} .. 2>&1 | tee -a configure.log
}

#Install Portion

if [ $(lsb_release --codename --short) != "jammy" ]; then
	EXTRAS="libavresample-dev libdc1394-22-dev"
fi
	 
apt-get update
apt-get install -y --no-install-recommends \
        build-essential \
	   gfortran \
        cmake \
        git \
	   file \
	   tar \
        libatlas-base-dev \
        libavcodec-dev \
        libavformat-dev \
        libcanberra-gtk3-module \
        libeigen3-dev \
        libglew-dev \
        libgstreamer-plugins-base1.0-dev \
        libgstreamer-plugins-good1.0-dev \
        libgstreamer1.0-dev \
        libgtk-3-dev \
        libjpeg-dev \
        libjpeg8-dev \
        libjpeg-turbo8-dev \
        liblapack-dev \
        liblapacke-dev \
        libopenblas-dev \
        libpng-dev \
        libpostproc-dev \
        libswscale-dev \
        libtbb-dev \
        libtbb2 \
        libtesseract-dev \
        libtiff-dev \
        libv4l-dev \
        libxine2-dev \
        libxvidcore-dev \
        libx264-dev \
	   libgtkglext1 \
	   libgtkglext1-dev \
        pkg-config \
        qv4l2 \
        v4l-utils \
        zlib1g-dev \
	   $EXTRAS

if [ $ARCH != "x86_64" ]; then
	echo "detected $ARCH, installing python3 dev packages..."

	apt-get install -y --no-install-recommends \
		python3-pip \
		python3-dev \
		python3-numpy \
		python3-distutils \
		python3-setuptools
fi

main () {

    local VER=${DEFAULT_VERSION}

    # parse arguments
    if [[ "$#" -gt 0 ]] ; then
        VER="$1"  # override the version
    fi

    if [[ "$#" -gt 1 ]] && [[ "$2" == "test" ]] ; then
        DO_TEST=1
    fi

    # prepare for the build:
    setup
    install_dependencies
    git_source ${VER}

    #if [[ ${DO_TEST} ]] ; then
    #    configure test
    #else
    #    configure
    #fi

    # start the build
    make -j${JOBS} 2>&1 | tee -a build.log

    #if [[ ${DO_TEST} ]] ; then
    #    make test 2>&1 | tee -a test.log
    #fi

    # avoid a sudo make install (and root owned files in ~) if $PREFIX is writable
    if [[ -w ${PREFIX} ]] ; then
        make install 2>&1 | tee -a install.log
    else
        sudo make install 2>&1 | tee -a install.log
    fi

    #cleanup --test-warning

}

main "$@"