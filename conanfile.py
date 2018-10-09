#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class FFTWConan(ConanFile):
    name = "fftw"
    version = "3.3.8"
    description = "C subroutine library for computing the Discrete Fourier Transform (DFT) in one or more dimensions"
    url = "https://github.com/bincrafters/conan-fftw"
    homepage = "http://www.fftw.org/"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "GPL-2.0"
    exports = ["COPYRIGHT"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False], "precision": ["double", "single", "longdouble"],
               "openmp": [True, False], "threads": [True, False], "combinedthreads": [True, False]}
    default_options = "shared=False", "fPIC=True", "precision=double", "openmp=False", "threads=False", \
                      "combinedthreads=False"
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        source_url = "http://www.fftw.org"
        tools.get("{0}/fftw-{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTS"] = "OFF"
        cmake.definitions["ENABLE_OPENMP"] = "ON" if self.options.openmp else "OFF"
        cmake.definitions["ENABLE_THREADS"] = "ON" if self.options.threads else "OFF"
        cmake.definitions["WITH_COMBINED_THREADS"] = "ON" if self.options.combinedthreads else "OFF"
        if self.options.precision == "single":
            cmake.definitions["ENABLE_FLOAT"] = "ON"
        elif self.options.precision == "longdouble":
            cmake.definitions["ENABLE_LONG_DOUBLE"] = "ON"
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="COPYRIGHT", dst="licenses", src=self._source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        # allow access to FFTW3*.cmake files for find_package(FFTW3 CONFIG) when using cmake_paths generator
        self.cpp_info.builddirs = ["", "lib/cmake/fftw3"]
