#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2018-12-23.
#  2018, SMART Health IT.


from . import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ Record of use of a device.
    
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    
    resource_type = "DeviceUseStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        
        """ Fulfills plan, proposal or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.derivedFrom = None
        
        """ Supporting information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.device = None
        
        """ Reference to device used.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ External identifier for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None
        
        """ Addition details (comments, instructions).
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        
        """ Why device was used.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        
        """ Why was DeviceUseStatement performed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recordedOn = None
        
        """ When statement was recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._recordedOn = None
        
        """ extension for fhir primitive  recordedOn"""
        
        self.source = None
        
        """ Who made the statement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | completed | entered-in-error +.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subject = None
        
        """ Patient using device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        
        """ How often  the device was used.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._timingDateTime = None
        
        """ extension for fhir primitive  timingDateTime"""
        
        self.timingPeriod = None
        
        """ How often  the device was used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        
        """ How often  the device was used.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(DeviceUseStatement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recordedOn", "recordedOn", FHIRDate, False, None, False),
            ("_recordedOn", "_recordedOn",fhirprimitive.FHIRPrimitive, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("_timingDateTime", "_timingDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period
from . import timing
from . import fhirprimitive

