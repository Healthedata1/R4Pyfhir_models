#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/DeviceMetric) on 2018-12-23.
#  2018, SMART Health IT.


from . import domainresource

class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.
    
    Describes a measurement, calculation or setting capability of a medical
    device.
    """
    
    resource_type = "DeviceMetric"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.calibration = None
        
        """ Describes the calibrations that have been performed or that are
        required to be performed.
        List of `DeviceMetricCalibration` items (represented as `dict` in JSON). """
        
        self.category = None
        
        """ measurement | setting | calculation | unspecified.
        Type `str`. """
        
        self._category = None
        
        """ extension for fhir primitive  category"""
        
        self.color = None
        
        """ black | red | green | yellow | blue | magenta | cyan | white.
        Type `str`. """
        
        self._color = None
        
        """ extension for fhir primitive  color"""
        
        self.identifier = None
        
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.measurementPeriod = None
        
        """ Describes the measurement repetition time.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.operationalStatus = None
        
        """ on | off | standby | entered-in-error.
        Type `str`. """
        
        self._operationalStatus = None
        
        """ extension for fhir primitive  operationalStatus"""
        
        self.parent = None
        
        """ Describes the link to the parent Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        
        """ Describes the link to the source Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Identity of metric, for example Heart Rate or PEEP Setting.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        
        """ Unit of Measure for the Metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceMetric, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceMetric, self).elementProperties()
        js.extend([
            ("calibration", "calibration", DeviceMetricCalibration, True, None, False),
            ("category", "category", str, False, None, True),
            ("_category", "_category",fhirprimitive.FHIRPrimitive, False, None, False),
            ("color", "color", str, False, None, False),
            ("_color", "_color",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("measurementPeriod", "measurementPeriod", timing.Timing, False, None, False),
            ("operationalStatus", "operationalStatus", str, False, None, False),
            ("_operationalStatus", "_operationalStatus",fhirprimitive.FHIRPrimitive, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class DeviceMetricCalibration(backboneelement.BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """
    
    resource_type = "DeviceMetricCalibration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.state = None
        
        """ not-calibrated | calibration-required | calibrated | unspecified.
        Type `str`. """
        
        self._state = None
        
        """ extension for fhir primitive  state"""
        
        self.time = None
        
        """ Describes the time last calibration has been performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._time = None
        
        """ extension for fhir primitive  time"""
        
        self.type = None
        
        """ unspecified | offset | gain | two-point.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(DeviceMetricCalibration, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend([
            ("state", "state", str, False, None, False),
            ("_state", "_state",fhirprimitive.FHIRPrimitive, False, None, False),
            ("time", "time", FHIRDate, False, None, False),
            ("_time", "_time",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import timing
from . import fhirprimitive

