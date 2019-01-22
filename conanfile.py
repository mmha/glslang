from conans import ConanFile, CMake, tools
import os

class GLSlangConan(ConanFile):
    name = "glslang"
    settings = "os", "arch", "build_type", "compiler"
    version = "7.10.2984"
    exports_sources = "*", "!.git"
    no_copy_source = True
    options = {
        "shared": [False, True],
        "spvremapper": [False, True],
        "amd_extensions": [False, True],
        "glslang_binaries": [False, True],
        "nv_extensions": [False, True],
        "hlsl": [False, True],
        "opt": [False, True],
    }
    default_options = {
        "shared": True,
        "spvremapper": True,
        "amd_extensions": True,
        "glslang_binaries": True,
        "nv_extensions": True,
        "hlsl": True,
        "opt": True
    }

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_SPVREMAPPER"] = self.options.spvremapper
        cmake.definitions["ENABLE_AMD_EXTENSIONS"] = self.options.amd_extensions
        cmake.definitions["ENABLE_GLSLANG_BINARIES"] = self.options.glslang_binaries
        cmake.definitions["ENABLE_NV_EXTENSIONS"] = self.options.nv_extensions
        cmake.definitions["ENABLE_HLSL"] = self.options.hlsl
        cmake.definitions["ENABLE_OPT"] = self.options.opt
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
