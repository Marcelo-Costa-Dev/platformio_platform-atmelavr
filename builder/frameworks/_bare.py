# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# Default flags for bare-metal programming (without any framework layers)
#

from SCons.Script import Import

Import("env")

env.Append(
    ASPPFLAGS=["-x", "assembler-with-cpp"],

    CFLAGS=[
        "-std=gnu11",
        "-fno-fat-lto-objects"
    ],

    CCFLAGS=[
        "-Os",  # optimize for size
        "-Wall",  # show warnings
        "-ffunction-sections",  # place each function in its own section
        "-fdata-sections",
        "-flto",
        "-mmcu=$BOARD_MCU"
    ],

    CXXFLAGS=[
        "-Wno-error=narrowing",
        "-fno-exceptions",
        "-fno-threadsafe-statics",
        "-fpermissive",
        "-std=gnu++11"
    ],

    CPPDEFINES=[
        ("F_CPU", "$BOARD_F_CPU")
    ],

    LINKFLAGS=[
        "-Os",
        "-mmcu=$BOARD_MCU",
        "-Wl,--gc-sections",
        "-flto",
        "-fuse-linker-plugin"
    ],

    LIBS=["m"]
)

# Duplicate preprocessor flags to the assembler
# for '.S', '.spp', '.SPP', '.sx' source files
env.Append(
    ASPPFLAGS=env.get("CCFLAGS", [])
)