[![Download](https://api.bintray.com/packages/bincrafters/public-conan/fftw%3Abincrafters/images/download.svg) ](https://bintray.com/bincrafters/public-conan/fftw%3Abincrafters/_latestVersion)
[![Build Status](https://travis-ci.org/bincrafters/conan-fftw.svg?branch=conan%2F3.3.8)](https://travis-ci.org/bincrafters/conan-fftw)
[![Build status](https://ci.appveyor.com/api/projects/status/github/bincrafters/conan-fftw?branch=conan%2F3.3.8&svg=true)](https://ci.appveyor.com/project/bincrafters/conan-fftw)

[Conan.io](https://conan.io) package recipe for [*fftw*](http://www.fftw.org/).

C subroutine library for computing the Discrete Fourier Transform (DFT) in one or more dimensions

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/bincrafters/public-conan/fftw%3Abincrafters).

## For Users: Use this package

### Basic setup

    $ conan install fftw/3.3.8@bincrafters/conan

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    fftw/3.3.8@bincrafters/conan

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create bincrafters/conan


### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |
| fPIC      | True |  [True, False] |
| precision      | double |  ['double', 'single', 'longdouble'] |
| openmp      | False |  [True, False] |
| threads      | False |  [True, False] |
| combinedthreads      | False |  [True, False] |

## Add Remote

    $ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload

    $ conan upload fftw/3.3.8@bincrafters/conan --all -r bincrafters


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package fftw.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](https://github.com/bincrafters/conan-fftw.git/blob/stable/3.3.8/LICENSE)
