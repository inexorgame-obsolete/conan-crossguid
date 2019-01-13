project(MyHello)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
set(CMAKE_CXX_STANDARD 11)

if (MSVC)
  add_definitions(/MP)
endif (MSVC)

add_executable(Test Test.cpp)
target_link_libraries(Test ${CONAN_LIBS})

