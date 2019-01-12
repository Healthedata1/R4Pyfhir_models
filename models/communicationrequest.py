#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/CommunicationRequest) on 2018-12-23.
#  2018, SMART Health IT.


from . import domainresource

class CommunicationRequest(domainresource.DomainResource):
    """ A request for information to be sent to a receiver.
    
    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """
    
    resource_type = "CommunicationRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.about = None
        
        """ Resources that pertain to this communication request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.authoredOn = None
        
        """ When request transitioned to being actionable.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._authoredOn = None
        
        """ extension for fhir primitive  authoredOn"""
        
        self.basedOn = None
        
        """ Fulfills plan or proposal.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Message category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.doNotPerform = None
        
        """ True if request is prohibiting action.
        Type `bool`. """
        
        self._doNotPerform = None
        
        """ extension for fhir primitive  doNotPerform"""
        
        self.encounter = None
        
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medium = None
        
        """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        
        """ Comments made about communication request.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        
        """ When scheduled.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self._occurrenceDateTime = None
        
        """ extension for fhir primitive  occurrenceDateTime"""
        
        self.occurrencePeriod = None
        
        """ When scheduled.
        Type `Period` (represented as `dict` in JSON). """
        
        self.payload = None
        
        """ Message payload.
        List of `CommunicationRequestPayload` items (represented as `dict` in JSON). """
        
        self.priority = None
        
        """ Message urgency.
        Type `str`. """
        
        self._priority = None
        
        """ extension for fhir primitive  priority"""
        
        self.reasonCode = None
        
        """ Why is communication needed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        
        """ Why is communication needed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recipient = None
        
        """ Message recipient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.replaces = None
        
        """ Request(s) replaced by this request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester = None
        
        """ Who/what is requesting service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sender = None
        
        """ Message sender.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ draft | active | suspended | cancelled | completed | entered-in-
        error | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.statusReason = None
        
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        
        """ Focus of message.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(CommunicationRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CommunicationRequest, self).elementProperties()
        js.extend([
            ("about", "about", fhirreference.FHIRReference, True, None, False),
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("_authoredOn", "_authoredOn",fhirprimitive.FHIRPrimitive, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("_doNotPerform", "_doNotPerform",fhirprimitive.FHIRPrimitive, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("_occurrenceDateTime", "_occurrenceDateTime",fhirprimitive.FHIRPrimitive, False, None, False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("payload", "payload", CommunicationRequestPayload, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority",fhirprimitive.FHIRPrimitive, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class CommunicationRequestPayload(backboneelement.BackboneElement):
    """ Message payload.
    
    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """
    
    resource_type = "CommunicationRequestPayload"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        
        """ Message part content.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        
        """ Message part content.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contentString = None
        
        """ Message part content.
        Type `str`. """
        
        self._contentString = None
        
        """ extension for fhir primitive  contentString"""
        
        super(CommunicationRequestPayload, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CommunicationRequestPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("contentString", "contentString", str, False, "content", True),
            ("_contentString", "_contentString",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import annotation
from . import attachment
from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period
from . import fhirprimitive
