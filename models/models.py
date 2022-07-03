# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from odoo.exceptions import ValidationError
import logging

from datetime import datetime


_logger = logging.getLogger(__name__)
class SudoAceCrm(models.Model):
    _inherit = 'crm.lead'

    submit_to_AWS = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'), ],
        string='Submit to AWS', default='No', required=True, copy=False,track_visibility='always')

    #industry_new = fields.Many2one('ace.industry', string='Industry')
    usecase = fields.Many2one(
        'ace.usecase', string='Use Case',track_visibility='always'
    )
    sub_usecase = fields.Many2one(
        'ace.subusecase', string='Sub Use Case',track_visibility='always'
    )

    # Because APN has different set of Lead use cases as compared to Opp
    lead_usecase = fields.Selection([
        ('Other', 'Other'),
    ], string='Lead Use Case', track_visibility='always')


    country_name = fields.Char("Country Name",track_visibility='always')

    partner_project_title = fields.Char(string='Partner Project Title', track_visibility='always')
    project_description = fields.Text(string='Project Description', track_visibility='always')

    partner_primary_need_from_aws = fields.Selection([
        ('Other', 'Other'),
    ], string='Need From AWS', track_visibility='always')
    partner_primary_needfromAWSOther = fields.Char(
        string='Specify Other Need',track_visibility='always'
    )

    currency_id = fields.Many2one('res.currency', string='Currency',track_visibility='always')

    expected_monthly_aws_revenue = fields.Monetary(string='Expected Monthly AWSRevenue', copy=False,track_visibility='always')
    target_close_date = fields.Date(string='Target CloseDate', copy=False,track_visibility='always')
    AWSCloseDate = fields.Date(string='AWS Close Date', copy=False,track_visibility='always')

    # delivery_model = fields.Selection([
    #     ('SaaS or PaaS', 'SaaS or PaaS'),
    #     ('BYOL or AMI', 'BYOL or AMI'),
    #     ('Managed Services', 'Managed Services'),
    #     ('Professional Services', 'Professional Services'),
    #     ('Resell', 'Resell'),
    #     ('Other', 'Other'),

    # ], string='Delivery Model', )

    delivery = fields.Many2many('ace.delivery',track_visibility='always')
    opportunity_owner_name = fields.Char(string='Opportunity Owner Name', copy=False,track_visibility='always')
    opportunity_owner_email = fields.Char(string='Opportunity Owner Email', copy=False,track_visibility='always')

    isnet_newbusiness_forcompany = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),

    ], string='isNetNewBusinessForCompany', copy=False,track_visibility='always')

    api_submission_status = fields.Selection([
        ('Success', 'Success'),
        ('Fail', 'Fail'),
    ], string='API Submission Status', copy=False,track_visibility='always')
    # Status is a read only field and its value depends on the type
    # The value will come from AWS.
    status = fields.Selection([
        ('Draft', 'Draft'),
        ('Submitted', 'Submitted'),
        ('In review', 'In review'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Action Required', 'Action Required'),

    ], string='APN AWS  Status', copy=False,track_visibility='always')
    lead_status = fields.Selection([
        ('Open', 'Open'),
        ('Research', 'Research'),
        ('Qualified', 'Qualified'),
        ('Disqualified', 'Disqualified'),

    ], string='Lead Status', copy=False,track_visibility='always')
    contract_vehicle = fields.Char(string='Contract Vehicle', copy=False,track_visibility='always')
    aws_leadSource = fields.Text(string='AWS Lead Source', copy=False,track_visibility='always')

    customer_title = fields.Char(string='Customer Title', default="Mr",track_visibility='always')
    closed_lost_reason = fields.Selection([

        ('Other', 'Other'),

    ], string='Closed Lost Reason', copy=False,track_visibility='always')

    aws_field_engagement = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),

    ], string='AWS Field Engagement', track_visibility='always')

    stage = fields.Selection([
        ('Business Validation', 'Business Validation'),

    ], string='APN Partner Stage', copy=False,track_visibility='always')

    rfx_solicitation_number = fields.Char(string='Solicitation Number',track_visibility='always')

    next_step = fields.Char(string='Next Step', copy=False)
    apn_crmunique_identifier = fields.Char(string='ACE OPP ID', copy=False,track_visibility='always')
    partner_crmunique_identifier = fields.Char(
        string='Partner CRM Unique Identifier',
        copy=False, track_visibility='always'
    )
    aws_account_id = fields.Char(string='AWS Account ID', copy=False,track_visibility='always')

    opportunity_ownership = fields.Selection([
        ('AWS Referral', 'AWS Referral'),
        ('Partner Referral', 'Partner Referral'),
    ], string='Opportunity Ownership', readonly=True, copy=False,track_visibility='always')

    isthis_apublic_reference = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),

    ], string='is This APublic Reference', copy=False,track_visibility='always' )
    public_referenceUrl = fields.Char(string='Public Reference URL', copy=False,track_visibility='always')
    public_referenceTitle = fields.Char(string='Public Reference Title', copy=False,track_visibility='always')

    is_this_for_resell = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),

    ], string='is This For Resell',track_visibility='always')



    partner_developer_manager_email = fields.Char(
        string='Partner Developer Manager Email',
        copy=False,track_visibility='always'
    )
    partnerDeveloperManager = fields.Char(string='Partner Developer Manager', copy=False,track_visibility='always')
    next_step_history = fields.Text(string='Next Step History', copy=False,track_visibility='always')



    is_this_for_marketplace = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'), ], string='Is This For Market Place',track_visibility='always')

    isMarketingDevelopmentFunded = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'), ],
        string='isMarketing DevelopmentFunded',track_visibility='always'
    )

    partner_acceptance_status = fields.Selection([
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'), ],
        string='Partner Acceptance Status',copy=False,track_visibility='always')

    competitive_tracking = fields.Selection([
        ('*Other', '*Other'),
    ], string='Competitive Tracking', track_visibility='always')

    aws_campaign_name = fields.Selection([
        ('Email Campaign - Products', 'Email Campaign - Products'),
    ], string='AWS Campaign Name', copy=False,track_visibility='always')


    competitiveTrackingOther = fields.Char(string='Competitive Tracking Other', track_visibility='always')

    aWSStage = fields.Char(string='AWS Stage', copy=False,track_visibility='always')

    aWSSalesRepName = fields.Char(string='AWS Sales Rep Name', copy=False,track_visibility='always')
    aWSSalesRepEmail = fields.Char(string='AWS Sales Rep  Email', copy=False,track_visibility='always')

    aWSPartnerSuccessManagerName = fields.Char(
        string='Partner Success Manager Name',
        copy=False,track_visibility='always'
    )
    aWSPartnerSuccessManagerEmail = fields.Char(
        string='Partner Success Manager Email',
        copy=False,track_visibility='always'
    )

    aWSISVSuccessManagerName = fields.Char(string='ISV Success Manager Name', copy=False,track_visibility='always')
    aWSISVSuccessManagerEmail = fields.Char(string='ISV Success Manager Email', copy=False,track_visibility='always')

    wWPSPDMEmail = fields.Char(string='PDM Email', copy=False,track_visibility='always')
    wWPSPDM = fields.Char(string='PDM Name', copy=False,track_visibility='always')

    aWSAccountOwnerName = fields.Char(string='Account Owner Name', copy=False,track_visibility='always')
    aWSAccountOwnerEmail = fields.Char(string='Account Owner Email', copy=False,track_visibility='always')


    current_lead_stage = fields.Selection([
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ], string='Current Lead Stage', copy=False,track_visibility='always')

    partner_crm_lead_id = fields.Integer(string="Partner Crm Lead Id",copy=False,track_visibility='always')
    segment_company_size = fields.Char(string="Segment Company Size",track_visibility='always')
    level_of_aws_usage = fields.Char(string="Level of AWS Usage",track_visibility='always')
    lead_status_reason = fields.Char(string="lead Status Reason",track_visibility='always')

    campaign_member_status = fields.Char(string="Campaign Member Status",track_visibility='always')
    lead_age = fields.Integer(string="Lead Age",copy=False,track_visibility='always')
    last_update_date = fields.Datetime(
        "Last update date",
       default=fields.Datetime.now,track_visibility='always'
       )
    sent_to_aws = fields.Boolean(
        'Sent to AWS',
        default=True,
        copy=False,track_visibility='always'
    )

    additionalComments = fields.Text(string="additionalComments",copy=False,track_visibility='always')
    aws_last_modified_by = fields.Text(string="AWS last modified by",copy=False,track_visibility='always')
    aws_last_modified_date = fields.Date(string="AWS last modified date",copy=False,track_visibility='always')
    website = fields.Char('Website',
                              help="Website of the contact",
                              readonly=False,track_visibility='always'
                              )
    check_ind_other = fields.Boolean('check other industry')
    is_public_sector = fields.Boolean('check other industry')
    industryothers = fields.Char(
        string='Industry Other',
        defaut=False,track_visibility='always'
    )
    apn_api_response = fields.Text(string="APN Response",copy=False,track_visibility='always')
    apn_api_response_history = fields.Text(string="APN Response History",copy=False)

    is_submitted = fields.Boolean(copy=False,track_visibility='always')
    is_launched = fields.Boolean(copy=False,track_visibility='always')
    is_closed_lost = fields.Boolean(copy=False,track_visibility='always')

    last_sent_to_aws_date = fields.Datetime(string="AWS Last Submission Time",copy=False,track_visibility='always')
    first_submission_to_aws_date = fields.Datetime(string="First Submission Time",copy=False,track_visibility='always')
    launch_submission_to_aws_date = fields.Datetime(string="Launch Submission Time",copy=False,track_visibility='always')

