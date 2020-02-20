#! /usr/bin/bash
mkdir -p submit
rm submit/*
./hashcode.py a_example.txt submit/a.txt
./hashcode.py b_read_on.txt submit/b.txt
./hashcode.py c_incunabula.txt submit/c.txt
./hashcode.py d_tough_choices.txt submit/d.txt
./hashcode.py e_so_many_books.txt submit/e.txt
./hashcode.py f_libraries_of_the_world.txt submit/f.txt
zip submit/code.zip *