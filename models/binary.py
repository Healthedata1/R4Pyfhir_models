#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Binary) on 2018-12-23.
#  2018, SMART Health IT.


from . import resource

class Binary(resource.Resource):
    """ Pure binary content defined by a format other than FHIR.
    
    A resource that represents the data of a single raw artifact as digital
    content accessible in its native format.  A Binary resource can contain any
    content, whether text, image, pdf, zip archive, etc.
    """
    
    resource_type = "Binary"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None
        
        """ MimeType of the binary content.
        Type `str`. """
        
        self._contentType = None
        
        """ extension for fhir primitive  contentType"""
        
        self.data = None
        
        """ The actual content.
        Type `str`. """
        
        self._data = None
        
        """ extension for fhir primitive  data"""
        
        self.securityContext = None
        
        """ Identifies another resource to use as proxy when enforcing access
        control.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Binary, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Binary, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, True),
            ("_contentType", "_contentType",fhirprimitive.FHIRPrimitive, False, None, False),
            ("data", "data", str, False, None, False),
            ("_data", "_data",fhirprimitive.FHIRPrimitive, False, None, False),
            ("securityContext", "securityContext", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import fhirreference
from . import fhirprimitive

