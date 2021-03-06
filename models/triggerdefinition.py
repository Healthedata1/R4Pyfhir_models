#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/TriggerDefinition) on 2018-12-23.
#  2018, SMART Health IT.


from . import element

class TriggerDefinition(element.Element):
    """ Defines an expected trigger for a module.
    
    A description of a triggering event. Triggering events can be named events,
    data events, or periodic, as determined by the type element.
    """
    
    resource_type = "TriggerDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.condition = None
        
        """ Whether the event triggers (boolean expression).
        Type `Expression` (represented as `dict` in JSON). """
        
        self.data = None
        
        """ Triggering data of the event (multiple = 'and').
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name or URI that identifies the event.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.timingDate = None
        
        """ Timing of the event.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._timingDate = None
        
        """ extension for fhir primitive  timingDate"""
        
        self.timingDateTime = None
        
        """ Timing of the event.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._timingDateTime = None
        
        """ extension for fhir primitive  timingDateTime"""
        
        self.timingReference = None
        
        """ Timing of the event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        
        """ Timing of the event.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ named-event | periodic | data-changed | data-added | data-modified
        | data-removed | data-accessed | data-access-ended.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(TriggerDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TriggerDefinition, self).elementProperties()
        js.extend([
            ("condition", "condition", expression.Expression, False, None, False),
            ("data", "data", datarequirement.DataRequirement, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timingDate", "timingDate", FHIRDate, False, "timing", False),
            ("_timingDate", "_timingDate",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("_timingDateTime", "_timingDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timingReference", "timingReference", fhirreference.FHIRReference, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import datarequirement
from . import expression
from . import fhirreference
from . import timing
from . import fhirprimitive

