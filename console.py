#!/usr/bin/python3
"""Command interpreter module"""
import cmd
import json
import os
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class to manipulte the "storage engine" """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User}

    def emptyline(self):
        """Overidden "emptyline" method"""

        pass

    def do_create(self, arg):
        """Creating an object, saving it into the file and
        printing its id"""

        if arg == '':
            print('** class name missing **')
        elif arg not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        else:
            obj = HBNBCommand.classes[arg]()
            obj.save()
            print(obj.id)

    do_new = do_create

    def do_show(self, arg):
        """Showing an object string representation based on
        the arguments class_name and object_id"""

        if not arg:
            print("** class name missing **")
        else:
            arguments = arg.split()
            cls_name = arguments[0]
            if cls_name not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print("** instance id missing **")
            else:
                object_id = arguments[1]
                json_file = FileStorage.__dict__['_FileStorage__file_path']
                if os.path.isfile(json_file):
                    with open(json_file, 'r', encoding='utf-8') as json_file:
                        json_str = json_file.read()
                        json_dict = json.loads(json_str)
                        if f'{cls_name}.{object_id}' not in json_dict.keys():
                            print("** no instance found **")
                        else:
                            classes = HBNBCommand.classes
                            target_dict = json_dict[f'{cls_name}.{object_id}']
                            target_obj = classes[cls_name](**target_dict)
                            print(target_obj)

    def do_destroy(self, arg):
        """Deleting an instance from the storage file"""

        file_name = FileStorage.__dict__['_FileStorage__file_path']
        if not arg:
            print("** class name missing **")
        else:
            arguments = arg.split()
            cls_name = arguments[0]
            if cls_name not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print("** instance id missing **")
            else:
                object_id = arguments[1]
                if os.path.isfile(file_name):
                    with open(file_name, 'r', encoding='utf-8') as json_file:
                        str_content = json_file.read()
                    dict_content = json.loads(str_content)
                    if f'{cls_name}.{object_id}' not in dict_content.keys():
                        print("** no instance found **")
                    else:
                        del dict_content[f'{cls_name}.{object_id}']
                        with open(file_name, 'w', encoding='utf-8') as j_file:
                            j_file.write(json.dumps(dict_content))
                        storage.reload()

    def do_all(self, arg):
        """Printing all a list of string representation of all
        the instances of the class "arg". If "arg" is missing,
        all the intances representation will be in the list"""

        classes = HBNBCommand.classes
        file_name = FileStorage.__dict__['_FileStorage__file_path']
        if os.path.isfile(file_name):
            with open(file_name, "r", encoding='utf-8') as json_file:
                str_content = json_file.read()
                dict_content = json.loads(str_content)
            objects_repr_list = []
            if arg:
                cls_name = arg
                if cls_name not in classes.keys():
                    print("** class doesn't exist **")
                else:
                    for key in dict_content.keys():
                        if f'{cls_name}' in key:
                            cls = classes[f'{cls_name}']
                            target_object = cls(**dict_content[key])
                            objects_repr_list.append(str(target_object))
                    print(objects_repr_list)
            else:
                for key in dict_content.keys():
                    cls_name = key.split('.')[0]
                    target_object = classes[cls_name](**dict_content[key])
                    objects_repr_list.append(str(target_object))
                print(objects_repr_list)

    def do_update(self, arg):
        """Updating inatance of "class_name" with the id "object_id"
        using the attribute "attr" with the value "value" one at a
        time. If "attr" doesn't exit, it will be created with the
        value "value" """

        types = [float, int, str, None, bool, dict, list, tuple, set, complex]
        file_name = FileStorage.__dict__['_FileStorage__file_path']
        classes = HBNBCommand.classes
        if not arg:
            print("** class name missing **")
        else:
            arguments = arg.split()
            cls_name = arguments[0]
            if cls_name not in classes:
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print("** instance id missing **")
            else:
                object_id = arguments[1]
                if os.path.isfile(file_name):
                    with open(file_name, 'r', encoding='utf-8') as json_file:
                        str_content = json_file.read()
                        dict_content = json.loads(str_content)
                    if f'{cls_name}.{object_id}' not in dict_content.keys():
                        print("** no instance found **")
                    else:
                        if len(arguments) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(arguments) < 4:
                                print("** value missing **")
                            else:
                                attr = arguments[2]
                                value = arguments[3]
                                tar_key = f'{cls_name}.{object_id}'
                                target = dict_content[tar_key]
                                if attr in target.keys():
                                    attr_type = type(target[attr])
                                    for the_type in types:
                                        if the_type == attr_type:
                                            target[attr] = the_type(value)
                                            f = file_name
                                            mode = {'encoding': 'utf-8'}
                                            with open(f, 'w', **mode) as jf:
                                                dict_content[tar_key] = target
                                                d_content = dict_content
                                                jf.write(json.dumps(d_content))
                                            break
                                        storage.reload()
                                else:
                                    tar_key = f'{cls_name}.{object_id}'
                                    target = dict_content[tar_key]
                                    target[attr] = value
                                f_name = file_name
                                with open(f_name, "r", encoding='utf-8') as jf:
                                    str_content = jf.read()
                                    dict_content = json.loads(str_content)
                                    dict_content[tar_key] = target
                                with open(f_name, 'w', encoding='utf-8') as jf:
                                    jf.write(json.dumps(dict_content))
                                storage.reload()

    def do_quit(self, arg):
        """Quitting the interpreter"""

        return 1

    def do_EOF(self, arg):
        """Quitting the interpreter"""

        print()
        return 1


if __name__ == "__main__":
    HBNBCommand().cmdloop()
