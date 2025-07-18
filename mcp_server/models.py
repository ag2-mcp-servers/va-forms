# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T11:28:32+00:00

from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class BenefitCategory(BaseModel):
    description: Optional[str] = Field(
        None,
        description='Description of the benefit category of the form',
        examples=['VA health care'],
    )
    name: Optional[str] = Field(
        None,
        description='Name of the benefit category of the form',
        examples=['Health care'],
    )


class Version(BaseModel):
    revision_on: Optional[date] = Field(
        None,
        description='The date the sha256 hash was calculated',
        examples=['2012-01-01'],
    )
    sha256: Optional[str] = Field(
        None,
        description='A sha256 hash of the form contents for that version',
        examples=['5fe171299ece147e8b456961a38e17f1391026f26e9e170229317bc95d9827b7'],
    )


class Attributes(BaseModel):
    benefit_categories: Optional[List[BenefitCategory]] = Field(
        None, description='Listing of benefit categories and match'
    )
    created_at: Optional[datetime] = Field(
        None,
        description='Internal field for VA.gov use',
        examples=['2021-03-30T16:28:30.338Z'],
    )
    deleted_at: Optional[datetime] = Field(
        None, description='The timestamp at which the form was deleted', examples=[None]
    )
    first_issued_on: Optional[date] = Field(
        None,
        description='The date the form first became available',
        examples=['2016-07-10'],
    )
    form_details_url: Optional[str] = Field(
        None,
        description='Location on www.va.gov of the info page for this form',
        examples=['https://www.va.gov/find-forms/about-form-10-10ez'],
    )
    form_name: Optional[str] = Field(
        None, description='Name of the VA Form', examples=['10-10EZ']
    )
    form_tool_intro: Optional[str] = Field(
        None,
        description='Introductory text describing the VA online tool for this form',
        examples=[
            'You can apply online instead of filling out and sending us the paper form.'
        ],
    )
    form_tool_url: Optional[str] = Field(
        None,
        description='Location of the online tool for this form',
        examples=['https://www.va.gov/health-care/apply/application/introduction'],
    )
    form_type: Optional[str] = Field(
        None, description='VA Type of the form', examples=['benefit']
    )
    form_usage: Optional[str] = Field(
        None,
        description='A description of how the form is to be used',
        examples=[
            '<p>Use VA Form 10-10EZ if you’re a Veteran and want to apply for VA health care. You must be enrolled in...</p>'
        ],
    )
    language: Optional[str] = Field(
        None, description='Language code of the form', examples=['en']
    )
    last_revision_on: Optional[date] = Field(
        None, description='The date the form was last updated', examples=['2020-01-17']
    )
    pages: Optional[int] = Field(
        None, description='Number of pages contained in the form', examples=[5]
    )
    related_forms: Optional[List[str]] = Field(
        None, description='A listing of other forms that relate to current form'
    )
    sha256: Optional[str] = Field(
        None,
        description='A sha256 hash of the form contents',
        examples=['5fe171299ece147e8b456961a38e17f1391026f26e9e170229317bc95d9827b7'],
    )
    title: Optional[str] = Field(
        None,
        description='Title of the form as given by VA',
        examples=['Instructions and Enrollment Application for Health Benefits'],
    )
    url: Optional[str] = Field(
        None,
        description='Web location of the form',
        examples=['https://www.va.gov/vaforms/medical/pdf/10-10EZ-fillable.pdf'],
    )
    va_form_administration: Optional[str] = Field(
        None,
        description='The VA organization that administers the form',
        examples=['Veterans Health Administration'],
    )
    valid_pdf: Optional[bool] = Field(
        None,
        description='A flag indicating whether the form url was confirmed as a valid download',
        examples=['true'],
    )
    versions: Optional[List[Version]] = Field(
        None, description='The version history of revisions to the form'
    )


class FormShow(BaseModel):
    attributes: Optional[Attributes] = None
    id: Optional[str] = Field(
        None, description='JSON API identifier', examples=['10-10-EZ']
    )
    type: Optional[str] = Field(
        None, description='JSON API type specification', examples=['va_form']
    )


class Attributes1(BaseModel):
    benefit_categories: Optional[List[BenefitCategory]] = Field(
        None, description='Listing of benefit categories and match'
    )
    deleted_at: Optional[datetime] = Field(
        None,
        description='The timestamp at which the form was deleted',
        examples=['null'],
    )
    first_issued_on: Optional[date] = Field(
        None,
        description='The date the form first became available',
        examples=['2016-07-10'],
    )
    form_details_url: Optional[str] = Field(
        None,
        description='Location on www.va.gov of the info page for this form',
        examples=['https://www.va.gov/find-forms/about-form-10-10ez'],
    )
    form_name: Optional[str] = Field(
        None, description='Name of the VA Form', examples=['10-10EZ']
    )
    form_tool_intro: Optional[str] = Field(
        None,
        description='Introductory text describing the VA online tool for this form',
        examples=[
            'You can apply online instead of filling out and sending us the paper form.'
        ],
    )
    form_tool_url: Optional[str] = Field(
        None,
        description='Location of the online tool for this form',
        examples=['https://www.va.gov/health-care/apply/application/introduction'],
    )
    form_type: Optional[str] = Field(
        None, description='VA Type of the form', examples=['benefit']
    )
    form_usage: Optional[str] = Field(
        None,
        description='A description of how the form is to be used',
        examples=[
            '<p>Use VA Form 10-10EZ if you’re a Veteran and want to apply for VA health care. You must be enrolled in...</p>'
        ],
    )
    language: Optional[str] = Field(
        None, description='Language code of the form', examples=['en']
    )
    last_revision_on: Optional[date] = Field(
        None, description='The date the form was last updated', examples=['2020-01-17']
    )
    last_sha256_change: Optional[date] = Field(
        None,
        description='The date of the last sha256 hash change',
        examples=['2019-05-30'],
    )
    pages: Optional[int] = Field(
        None, description='Number of pages contained in the form', examples=[5]
    )
    related_forms: Optional[List[str]] = Field(
        None, description='A listing of other forms that relate to current form'
    )
    sha256: Optional[str] = Field(
        None,
        description='A sha256 hash of the form contents',
        examples=['6e6465e2e1c89225871daa9b6d86b92d1c263c7b02f98541212af7b35272372b'],
    )
    title: Optional[str] = Field(
        None,
        description='Title of the form as given by VA',
        examples=['Instructions and Enrollment Application for Health Benefits'],
    )
    url: Optional[str] = Field(
        None,
        description='Web location of the form',
        examples=['https://www.va.gov/vaforms/medical/pdf/10-10EZ-fillable.pdf'],
    )
    va_form_administration: Optional[str] = Field(
        None,
        description='The VA organization that administers the form',
        examples=['Veterans Health Administration'],
    )
    valid_pdf: Optional[bool] = Field(
        None,
        description='A flag indicating whether the form url was confirmed as a valid download',
        examples=['true'],
    )


class FormsIndex(BaseModel):
    attributes: Optional[Attributes1] = None
    id: Optional[str] = Field(
        None, description='JSON API identifier', examples=['5403']
    )
    type: Optional[str] = Field(
        None, description='JSON API type specification', examples=['va_form']
    )


class FormsGetResponse(BaseModel):
    data: List[FormsIndex]


class FormsGetResponse1(BaseModel):
    message: Optional[str] = Field(
        None, examples=['Invalid authentication credentials']
    )


class FormsGetResponse2(BaseModel):
    message: Optional[str] = Field(None, examples=['API rate limit exceeded'])


class FormsFormNameGetResponse(BaseModel):
    data: FormShow


class FormsFormNameGetResponse1(BaseModel):
    message: Optional[str] = Field(
        None, examples=['Invalid authentication credentials']
    )


class Error(BaseModel):
    message: Optional[str] = Field(None, examples=['Form not found'])


class FormsFormNameGetResponse2(BaseModel):
    errors: List[Error]


class FormsFormNameGetResponse3(BaseModel):
    message: Optional[str] = Field(None, examples=['API rate limit exceeded'])
