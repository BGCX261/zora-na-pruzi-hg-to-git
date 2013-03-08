#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je třída, která ...
'''
#import lxml.etree
from . import __ELEMENT_SVG,  NAMESPACE

class SVG(__ELEMENT_SVG):
    
    TAG = '{{{}}}svg'.format(NAMESPACE)
#    TAG = lxml.etree.QName(NAMESPACE, 'svg')
    
    __viewBox = [0,  0,  800,  600]

    @property
    def šířka(self):
        return self.__viewBox[3]
        
    @property
    def výška(self):
        return self.__viewBox[4]
        
    @šířka.setter
    def šířka(self,  hodnota):
        if not isinstance(hodnota,  int):
            raise TypeError('ViewBox žádá zadat šířku jako číslo, nikolivěk {}'.format(type(hodnota)))
            
        self.__viewBox[3] = hodnota
        
    @výška.setter
    def výška(self,  hodnota):
        if not isinstance(hodnota,  int):
            raise TypeError('ViewBox žádá zadat šířku jako číslo, nikolivěk {}'.format(type(hodnota)))
            
        self.__viewBox[3] = hodnota
        
    def __str__(self):
        self.set('viewBox',  ' '.join(map(str,  self.__viewBox)))
        return super().__str__()
        
    def hlavička_souboru(self,  jméno_souboru):
        import lxml.etree
        
        xml_deklarace = self.xml_deklarace
        
        xml_stylesheet = lxml.etree.PI('xml-stylesheet', "href='{}' type='text/css'")
        xml_stylesheet = lxml.etree.tounicode(xml_stylesheet,  pretty_print=True)
        
        from zora_na_pruzi import __version__,  __author__
        from datetime import date
            
        def rok():
            letos = date.today().timetuple()[0]
            if letos > 2012:
                return '2012 - {}'.format(letos)
            else:
                return '2012'
            
        self.insert(0, lxml.etree.Comment('Изготовила Зора на прузи {verze} ©Домоглед {autor} {rok} on {datum}'.format(verze = __version__, datum = date.today().isoformat(),  autor = __author__,  rok = rok())))
        self.insert(1, lxml.etree.Comment('http://domogled.eu'))
        self.insert(2, lxml.etree.Comment('http://code.google.com/p/zora-na-pruzi/'))
        
        return '\n'.join((xml_deklarace,  xml_stylesheet))


#import io
#import os
#import json
#from datetime import date
#from numbers import Number
#from lxml import etree
#from math import cos, sin, pi
#from urllib.parse import urlparse
#from pygal.util import template, coord_format, minify_css
#from pygal import __version__
#
#
#class Svg(object):
#    """Svg object"""
#    ns = 'http://www.w3.org/2000/svg'
#
#    def __init__(self, graph):
#        self.graph = graph
#        self.processing_instructions = [
#            etree.PI('xml', "version='1.0' encoding='utf-8'")]
#        self.root = etree.Element(
#            "{%s}svg" % self.ns,
#            nsmap={
#                None: self.ns,
#                'xlink': 'http://www.w3.org/1999/xlink',
#            })
#        self.root.append(
#            etree.Comment('Generated with pygal %s ©Kozea 2012 on %s' % (
#                __version__, date.today().isoformat())))
#        self.root.append(etree.Comment('http://pygal.org'))
#        self.root.append(etree.Comment('http://github.com/Kozea/pygal'))
#        self.defs = self.node(tag='defs')
#
#    def add_styles(self):
#        """Add the css to the svg"""
#        for css in ['base.css'] + list(self.graph.css):
#            if urlparse(css).scheme:
#                self.processing_instructions.append(
#                    etree.PI(
#                        'xml-stylesheet', 'href="%s"' % css))
#            else:
#                if not os.path.exists(css):
#                    css = os.path.join(
#                        os.path.dirname(__file__), 'css', css)
#                with io.open(css, encoding='utf-8') as f:
#                    css_text = template(
#                        f.read(),
#                        style=self.graph.style,
#                        font_sizes=self.graph.font_sizes())
#                    if not self.graph.pretty_print:
#                        css_text = minify_css(css_text)
#                    self.node(
#                        self.defs, 'style', type='text/css').text = css_text
#
#    def add_scripts(self):
#        """Add the js to the svg"""
#        common_script = self.node(self.defs, 'script', type='text/javascript')
#        common_script.text = " = ".join(
#            ("window.config", json.dumps(self.graph.config.to_dict())))
#
#        for js in self.graph.js:
#            if urlparse(js).scheme:
#                self.node(
#                    self.defs, 'script', type='text/javascript', href=js)
#            else:
#                script = self.node(self.defs, 'script', type='text/javascript')
#                with io.open(js, encoding='utf-8') as f:
#                    script.text = f.read()
#
#    def node(self, parent=None, tag='g', attrib=None, **extras):
#        """Make a new svg node"""
#        if parent is None:
#            parent = self.root
#        attrib = attrib or {}
#        attrib.update(extras)
#
#        def in_attrib_and_number(key):
#            return key in attrib and isinstance(attrib[key], Number)
#
#        for pos, dim in (('x', 'width'), ('y', 'height')):
#            if in_attrib_and_number(dim) and attrib[dim] < 0:
#                attrib[dim] = - attrib[dim]
#                if in_attrib_and_number(pos):
#                    attrib[pos] = attrib[pos] - attrib[dim]
#
#        for key, value in list(attrib.items()):
#            if value is None:
#                del attrib[key]
#            elif not isinstance(value, str):
#                attrib[key] = str(value)
#            elif key.endswith('_'):
#                attrib[key.rstrip('_')] = attrib[key]
#                del attrib[key]
#            elif key == 'href':
#                attrib['{http://www.w3.org/1999/xlink}' + key] = attrib[key]
#                del attrib[key]
#        return etree.SubElement(parent, tag, attrib)
#
#    def transposable_node(self, parent=None, tag='g', attrib=None, **extras):
#        """Make a new svg node which can be transposed if horizontal"""
#        if self.graph.horizontal:
#            for key1, key2 in (('x', 'y'), ('width', 'height')):
#                attr1 = extras.get(key1, None)
#                attr2 = extras.get(key2, None)
#                extras[key1], extras[key2] = attr2, attr1
#        return self.node(parent, tag, attrib, **extras)
#
#    def line(self, node, coords, close=False, **kwargs):
#        """Draw a svg line"""
#        line_len = len(coords)
#        if line_len < 2:
#            return
#        root = 'M%s L%s Z' if close else 'M%s L%s'
#        origin_index = 0
#        while origin_index < line_len and None in coords[origin_index]:
#            origin_index += 1
#        if origin_index == line_len:
#            return
#        origin = coord_format(coords[origin_index])
#        line = ' '.join([coord_format(c)
#                         for c in coords[origin_index + 1:]
#                         if None not in c])
#        self.node(node, 'path',
#                  d=root % (origin, line), **kwargs)
#
#    def slice(
#            self, serie_node, node, radius, small_radius,
#            angle, start_angle, center, val):
#        """Draw a pie slice"""
#        project = lambda rho, alpha: (
#            rho * sin(-alpha), rho * cos(-alpha))
#        diff = lambda x, y: (x[0] - y[0], x[1] - y[1])
#        fmt = lambda x: '%f %f' % x
#        get_radius = lambda r: fmt(tuple([r] * 2))
#        absolute_project = lambda rho, theta: fmt(
#            diff(center, project(rho, theta)))
#
#        if angle == 2 * pi:
#            self.node(node, 'circle',
#                      cx=center[0],
#                      cy=center[1],
#                      r=radius,
#                      class_='slice reactive tooltip-trigger')
#        else:
#            to = [absolute_project(radius, start_angle),
#                  absolute_project(radius, start_angle + angle),
#                  absolute_project(small_radius, start_angle + angle),
#                  absolute_project(small_radius, start_angle)]
#            self.node(node, 'path',
#                      d='M%s A%s 0 %d 1 %s L%s A%s 0 %d 0 %s z' % (
#                          to[0],
#                          get_radius(radius), int(angle > pi), to[1],
#                          to[2],
#                          get_radius(small_radius), int(angle > pi), to[3]),
#                      class_='slice reactive tooltip-trigger')
#        x, y = diff(center, project(
#            (radius + small_radius) / 2, start_angle + angle / 2))
#
#        self.graph._tooltip_data(node, val, x, y, classes="centered")
#        self.graph._static_value(serie_node, val, x, y)
#
#    def pre_render(self):
#        """Last things to do before rendering"""
#        self.add_styles()
#        self.add_scripts()
#        self.root.set(
#            'viewBox', '0 0 %d %d' % (self.graph.width, self.graph.height))
#        if self.graph.explicit_size:
#            self.root.set('width', str(self.graph.width))
#            self.root.set('height', str(self.graph.height))
#
#    def draw_no_data(self):
#        no_data = self.node(self.graph.nodes['text_overlay'], 'text',
#                            x=self.graph.view.width / 2,
#                            y=self.graph.view.height / 2,
#                            class_='no_data')
#        no_data.text = self.graph.no_data_text
#
#    def render(self, is_unicode=False, pretty_print=False):
#        """Last thing to do before rendering"""
#        svg = etree.tostring(
#            self.root, pretty_print=pretty_print,
#            xml_declaration=False,
#            encoding='utf-8')
#        if not self.graph.disable_xml_declaration:
#            svg = b'\n'.join(
#                [etree.tostring(
#                    pi, encoding='utf-8', pretty_print=pretty_print)
#                 for pi in self.processing_instructions]
#            ) + b'\n' + svg
#        if self.graph.disable_xml_declaration or is_unicode:
#            svg = svg.decode('utf-8')
#        return svg