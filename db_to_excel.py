import sqlite3
import os
import  sys


class Image(object):

    def __init__(self):
        self.image_name = []

    def load_directory(self, path='/Users/soumilshah/IdeaProjects/Youtube/images'):
        """

        :param path: Provide Path of File Directory
        :return: List of image Names
        """
        for x in os.listdir(path):
            self.image_name.append(x)

        return self.image_name

    def create_database(self, name, image):
        """

        :param name: String
        :param image:  BLOP Data
        :return: None
        """

        conn = sqlite3.connect("Image.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_table 
        (name TEXT,image BLOP)""")

        cursor.execute(""" INSERT INTO my_table 
        (name, image) VALUES (?,?)""",(name,image))

        conn.commit()
        cursor.close()
        conn.close()


def main():
    obj = Image()
    os.chdir("/Users/soumilshah/IdeaProjects/Youtube/images")
    for x in obj.load_directory():

        if ".png" in x:
            with open(x,"rb") as f:
                data = f.read()
                obj.create_database(name=x, image=data)
                print("{} Added to database ".format(x))

        elif ".jpg" in x:
            with open(x,"rb") as f:
                data = f.read()
                obj.create_database(name=x,image=data)
                print("{} added to Database".format(x))

def fetch_data():
    counter = 1
    os.chdir("/Users/soumilshah/IdeaProjects/Youtube/images")
    conn = sqlite3.connect("Image.db")
    cursor = conn.cursor()

    data = cursor.execute("""SELECT * FROM my_table""")
    for x in data.fetchall():
        print(x[1])
        with open("{}.png".format(counter),"wb") as f:
            f.write(x[1])
            counter= counter + 1


    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    fetch_data()