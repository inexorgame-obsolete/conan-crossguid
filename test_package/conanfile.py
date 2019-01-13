from conans import ConanFile, CMake
import os

channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "inexorgame")

class CrossguidTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "crossguid/latest-at-28-12-18@{}/{}".format(username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.source_folder, build_dir='./')
        cmake.build()

    def test(self):
        self.run(os.path.join(".", "bin", "Test"))
