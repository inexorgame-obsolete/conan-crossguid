from conans import ConanFile, CMake, tools
import os


class Conan(ConanFile):
    name = "crossguid"
    version = "latest-at-28-12-18"
    license = "MIT"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    requires = None


    def requirements(self):
        if self.settings.os == "Linux":
            self.requires("libuuid/1.0.3@bincrafters/stable")

    def source(self):
        self.run("git clone --branch master --depth 1 https://github.com/graeme-hill/crossguid")
        tools.replace_in_file("crossguid/CMakeLists.txt", "project(CrossGuid)", '''project(CrossGuid)
        include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
        conan_basic_setup()''')


    def build(self):
        cmake = CMake(self)
        cmake.definitions["CROSSGUID_TESTS"] = False
        self.run("cmake crossguid {}".format(cmake.command_line))
        self.run("cmake --build . {}".format(cmake.build_config))

    def package(self):
        self.copy("*", src="crossguid/include", dst="include")
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["crossguid-dgb" if self.settings.build_type == "Debug" else "crossguid"]

