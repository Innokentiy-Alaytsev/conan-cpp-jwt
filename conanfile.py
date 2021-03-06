#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class CppJwtConan(ConanFile):
    name = "cpp-jwt"
    version = "1.0.1"
    url = "https://github.com/DEGoodmanWilson/conan-cpp-jwt"
    description = "A C++ library for handling JWT tokens"
    license = "https://github.com/arun11299/cpp-jwt/blob/master/LICENSE"
    no_copy_source = True
    build_policy = "always"
    requires = "OpenSSL/1.0.2n@conan/stable", "jsonformoderncpp/[~= 3.1]@vthiery/stable"

    def source(self):
        source_url = "https://github.com/arun11299/cpp-jwt"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, "sources")
        #Rename to "sources" is a convention to simplify later steps

    def package_id(self):
        self.info.header_only()

    def package(self):
        self.copy(pattern="LICENSE")
        self.copy(pattern="*.[i|h]pp", dst="include", src="sources/include", keep_path=True)
