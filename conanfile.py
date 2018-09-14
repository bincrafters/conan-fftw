#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class FFTWConan(ConanFile):
    name = "fftw"
    version = "3.3.8"
    description = "C subroutine library for computing the discrete Fourier transform (DFT) in one or more dimensions"
    url = "https://github.com/hlysunnaram/conan-fftw"
    homepage = "https://github.com/FFTW/fftw3"
    author = "Herve Ly-Sunnaram <herve.ly-sunnaram@c-s.fr>"
    license = "GPL-2.0"
    exports = ["COPYRIGHT"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False], "precision": ["double", "single", "longdouble"]}
    default_options = "shared=False", "fPIC=True", "precision=double"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        source_url = "http://www.fftw.org"
        tools.get("{0}/fftw-{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        if self.options.precision == "single":
            cmake.definitions["ENABLE_FLOAT"] = "ON"
        elif self.options.precision == "longdouble":
            cmake.definitions["ENABLE_LONG_DOUBLE"] = "ON"
        if self.settings.os != 'Windows':
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="COPYRIGHT", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        # allow access to FFTW3*.cmake files for find_package(FFTW3 CONFIG) when using cmake_paths generator
        self.cpp_info.builddirs = ["", "lib/cmake/fftw3"]
