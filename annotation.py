#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:31:06 2018

@author: alpha
"""

import glob, os
from xml.dom.minidom import parseString
import PIL.Image

class Label:
    def __init__(self, X1, Y1, X2, Y2, X3, Y3, X4, Y4, text):
        self.X1 = float(X1)
        self.Y1 = float(Y1)
        self.X2 = float(X2)
        self.Y2 = float(Y2)
        self.X3 = float(X3)
        self.Y3 = float(Y3)
        self.X4 = float(X4)
        self.Y4 = float(Y4)
        self.text = text
    
    def output(self):
        print('X1, Y1: %s,%s'%(self.X1, self.X1))
        print('X2, Y2: %s,%s'%(self.X2, self.Y2))
        print('X3, Y3: %s,%s'%(self.X3, self.Y3))
        print('X4, Y4: %s,%s'%(self.X4, self.Y4))
        print('Text: %s'% self.text)

    def to_textbox_dictionary(self):
        textbox_text_annotation = {}
        textbox_text_annotation['text'] = self.text
        textbox_text_annotation['xmax'] = str(int(self.X1))
        textbox_text_annotation['ymax'] = str(int(self.Y1))
        textbox_text_annotation['xmin'] = str(int(self.X3))
        textbox_text_annotation['ymin'] = str(int(self.Y3))
        return textbox_text_annotation

class Annotation:
    
    def __init__(self):
        self.loaded = False
        self.annotations = {}

    def load_data(self):
        annotation_dir_name = './train/annotation'
        os.chdir(annotation_dir_name)

        list_of_files = []
        for file in glob.glob("*.txt"):
            list_of_files.append(file)
        
    
        for anno_file_name in list_of_files:
            annotation_file = open(anno_file_name, 'r', encoding='utf8')
            anno_file_name_with_out_format = anno_file_name.split('.txt')[0]
            annotations = []
            for line in annotation_file:
                annotation = [tmp for tmp in line[:-2].split(',')]
                annotation = Label(
                                    annotation[0], annotation[1], 
                                    annotation[2], annotation[3], 
                                    annotation[4], annotation[5],
                                    annotation[6], annotation[7],
                                    annotation[8])
                annotations.append(annotation)
            self.annotations[anno_file_name_with_out_format] =  annotations
            annotation_file.close()

    def write_to_json(self, file_name = 'annotation.json'):
        pass
    
    
    def write_to_xml(self, dir_name = 'xml_annotation/'):
        dir_name = './../' + dir_name
        def textbox_to_xml(x):
            res = '            <object><bndbox>\n'
            res += '                <name>%s</name>\n'%x['text']
            res += '                <xmin>%s</xmin>\n'%x['xmin']
            res += '                <ymin>%s</ymin>\n'%x['ymin']
            res += '                <xmax>%s</xmax>\n'%x['xmax']
            res += '                <ymax>%s</ymax>\n'%x['ymax']
            res += '            </bndbox></object>\n'
            
            return res
        
        for key, annotations in self.annotations.items():
            print('*'*10 + key + '*'*10)
            
            img = PIL.Image.open('./../img/' + key + '.jpg')
            width, height = img.size
            depth = len(img.getbands())
            
            output = '<?xml version="1.0" encoding="utf-8"?>\n'
            output += '<annotation>\n'
            output += '            <folder></folder>\n'
            output += '            <filename>%s</filename>\n'%(key + '.jpg')
            output += '''
            <size>
                <width>%i</width>
                <height>%i</height>
                <depth>%i</depth>
            </size>\n
            '''%(width, height, depth)
            
            
            output += '\n'
            for annotation in annotations:
                #annotation.output()
                output += textbox_to_xml(annotation.to_textbox_dictionary())
                output += '\n'
            
            output += '</annotation>'
            
            
            fout = open(dir_name + key + '.xml','w')
            fout.write(output)
            fout.close()

    
    
anno = Annotation()
anno.load_data()
anno.write_to_xml()


#    xml = dicttoxml(annotations)
 #   print(xml)