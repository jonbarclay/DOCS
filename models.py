from django.db import models
from datetime import datetime, timedelta
from django.template.defaultfilters import slugify
from django.forms import ModelForm
import markdown


class SAQ(models.Model):
    saq_name = models.CharField(max_length=200)
    saq_version = models.CharField(max_length=200)
    saq_risk = models.IntegerField(blank=True, null=True, default=0)
    saq_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.saq_version + " " + self.saq_name


class Merchant(models.Model):
    merchant_name = models.CharField(max_length=200)
    merchant_name_URL = models.CharField(max_length=200, null=True, blank=True, default='')
    merch_percent = models.FloatField(null=True, blank=True, default=0)
    req_complete = models.IntegerField(blank=True, null=True, default=0)
    total_req = models.IntegerField(blank=True, null=True, default=0)
    merchant_URL = models.URLField(max_length=2000, blank=True, null=True)
    merchant_contact_name = models.CharField(max_length=100, blank=True, null=True)
    merchant_contact_uvid = models.CharField(max_length=8, blank=True, null=True)
    merchant_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    merchant_contact_email = models.EmailField(blank=True, null=True)
    merchant_business_description = models.TextField(blank=True, null=True, help_text="Description of the merchant’s payment card business. This is not intended to be a cut-and-paste from the department’s website, but should be a tailored description that shows the assessor understands the business of the merchant being assessed.")
    merchant_card_processing_description = models.TextField(blank=True, null=True, help_text="Describe how and why the merchant stores, processes, and/or transmits cardholder data. This is not intended to be a cut-and-paste from above, but should build on the understanding of the business and the impact this can have upon the security of cardholder data.")
#    merchant_payment_channels = models.TextField(blank=True, null=True, help_text="What types of payment channels the merchant serves, such as card-present and card-not-present (for example, mail order/telephone order (MOTO), e-commerce).")
    merchant_third_parties = models.TextField(blank=True, null=True, help_text="Any entities that the assessed merchant connects to for payment transmission or processing, including processor relationships.")
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    merchant_network_diagram = models.FileField(upload_to='network-diagram', blank=True, null=True, help_text="Provide a high-level network diagram (either obtained from the entity or created by assessor) of the entity’s networking topography, showing the overall architecture of the environment being assessed. This high-level diagram should summarize all locations and key systems, and the boundaries between them and should include the following: Connections into and out of the network including demarcation points between the cardholder data environment (CDE) and other networks/zones Critical components within the cardholder data environment, including POS devices, systems, databases, and web servers, as applicable Other necessary payment components, as applicable")
    merchant_process_identify_data = models.TextField(blank=True, null=True, help_text="Describe the methods or processes (for example, tools, observations, feedback, scans, data flow analysis) used to identify and document all existences of cardholder data (as executed by the assessor, assessed entity or a combination):")
    merchant_process_no_data_outside_cde = models.TextField(blank=True, null=True, help_text="Describe the methods or processes (for example, tools, observations, feedback, scans, data flow analysis) used to verify that no cardholder data exists outside of the defined CDE (as executed by the assessor, assessed entity or a combination):")
    merchant_scope_review_process = models.TextField(blank=True, null=True, help_text="Describe how the results of the methods/processes were evaluated by the assessor to verify that the PCI DSS scope of review is appropriate:")
    merchant_scope_documentation = models.TextField(blank=True, null=True, help_text="Describe how the results of the methods/processes were documented (for example, the results may be a diagram or an inventory of cardholder data locations):")
    merchant_scope_reasoning = models.TextField(blank=True, null=True, help_text="Describe why the methods (for example, tools, observations, feedback, scans, data flow analysis) used for scope verification are considered by the assessor to be effective and accurate:")
    merchant_cde_people = models.TextField(blank=True, null=True, help_text="People – such as technical support, management, administrators, operations teams, cashiers, telephone operators, etc.: Note – this is not intended to be a list of individuals interviewed, but instead a list of the types of people, teams, etc. who were included in the scope.")
    merchant_cde_processes = models.TextField(blank=True, null=True, help_text="Processes – such as payment channels, business functions, etc.:")
    merchant_cde_technologies = models.TextField(blank=True, null=True, help_text="Technologies – such as e-commerce systems, internal network segments, DMZ segments, processor connections, POS systems, etc.: Note – this is not intended to be a list of devices but instead a list of the types of technologies, purposes, functions, etc. included in the scope.")
    merchant_cde_locations = models.TextField(blank=True, null=True, help_text="Locations/sites/stores – such as retail outlets, data centers, corporate office locations, call centers, etc.:")
    merchant_network_segmentation = models.TextField(blank=True, null=True, help_text="Identify whether the assessed entity has used network segmentation to reduce the scope of the assessment. (yes/no) Explain how the assessor validated the effectiveness of the segmentation, as follows: Describe the methods used to validate the effectiveness of the segmentation (for example, observed configurations of implemented technologies, tools used, network traffic analysis, etc.). Describe how it was verified that the segmentation is functioning as intended. Describe how it was verified that adequate security controls are in place to ensure the integrity of the segmentation mechanisms (e.g., access controls, change management, logging, monitoring, etc.).")
    merchant_cde_networks = models.TextField(blank=True, null=True, help_text="Describe all networks that store, process and/or transmit CHD:")
    merchant_in_scope_networks = models.TextField(blank=True, null=True, help_text="Describe all networks that do not store, process and/or transmit CHD, but are still in scope (e.g., connected to the CDE or provide management functions to the CDE):")
    merchant_out_of_scope_networks = models.TextField(blank=True, null=True, help_text="Describe any networks confirmed to be out of scope:")
    merchant_processing_entities = models.TextField(blank=True, null=True, help_text="Identify All Processing Entities (Acquirer/ Bank/ Brands directly connected to for processing)")
    merchant_wireless = models.TextField(blank=True, null=True, help_text="If there are no wireless networks or technologies in use, describe how this was verified by the assessor. If there are wireless networks or technologies in use, identify and describe all wireless technologies in use that are connected to or could impact the security of the cardholder data environment. This would include : Wireless LANs, Wireless payment applications (for example, POS terminals), All other wireless devices/technologies")
    merchant_data_flow_authorization = models.TextField(blank=True, null=True, help_text="Describe how cardholder data is transmitted and/or processed and for what purpose it is used")
    merchant_data_flow_capture = models.TextField(blank=True, null=True, help_text="Describe how cardholder data is transmitted and/or processed and for what purpose it is used")
    merchant_data_flow_settlement = models.TextField(blank=True, null=True, help_text="Describe how cardholder data is transmitted and/or processed and for what purpose it is used")
    merchant_data_flow_chargeback = models.TextField(blank=True, null=True, help_text="Describe how cardholder data is transmitted and/or processed and for what purpose it is used")
    merchant_card_storage = models.TextField(blank=True, null=True, help_text="Identify and list all databases, tables, and files storing cardholder data and provide the following details. Note: The list of files and tables that store cardholder data in the table below must be supported by an inventory created (or obtained from the client) and retained by the assessor in the work papers.")
    merchant_sampling = models.TextField(blank=True, null=True, help_text="Identify whether sampling was used during the assessment. Describe the sampling rationale and/or standardized PCI DSS security and operational processes/controls used for selecting sample sizes (for people, processes, technologies, devices, locations/sites, etc.).")

#    saq_a = 'A'
#    saq_aep = 'A-EP'
#    saq_b = 'B'
#    saq_c = 'C'
#    saq_cvt = 'C-VT'
#    saq_d = 'D'
#    saq_p2pe = 'P2PE'
#
#    saq_choices = (
#        (saq_a, 'SAQ A'),
#        (saq_aep, 'SAQ A-EP'),
#        (saq_b, 'SAQ B'),
#        (saq_c, 'SAQ C'),
#        (saq_cvt, 'SAQ C-VT'),
#        (saq_d, 'SAQ D'),
#        (saq_p2pe, 'SAQ P2PE'),
#    )
#    saq_req =models.CharField(max_length=4,
#                            choices=saq_choices,
#                            default=saq_d)
    saq_req = models.ForeignKey(SAQ, blank=True, null=True)

    def __str__(self):
        return self.merchant_name

    def save(self, *args, **kwargs):
        self.merchant_name_URL = slugify(self.merchant_name)
        super(Merchant, self).save(*args, **kwargs) # Call the "real" save() method.

    class Meta:
        ordering = ["merchant_name"]


class Hardware(models.Model):
    hardware_device_type = models.CharField(max_length=200, help_text="Identify and list all types of hardware in the cardholder environment, including network components, servers and other mainframes, devices performing security functions, end-user devices (such as laptops and workstations), virtualized devices (if applicable) and any other critical hardware – including homegrown components. For each item in the list, provide details for the hardware as indicated below. Add rows, as needed.")
    hardware_vendor = models.TextField(blank=True, null=True)
    hardware_role = models.TextField(blank=True, null=True)

    merchants = models.ManyToManyField(Merchant)

    def __str__(self):
        return self.hardware_device_type
    class Meta:
        verbose_name_plural = "hardware"


class Software(models.Model):
    software_product = models.CharField(max_length=200, help_text="Identify and list all critical software in the cardholder environment, such as e-commerce applications, applications accessing CHD for non-payment functions (fraud modeling, credit verification, etc.), software performing security functions or enforcing PCI DSS controls, underlying operating systems that store, process or transmit CHD, system management software, virtualization management software, and other critical software – including homegrown software/applications. For each item in the list, provide details for the software as indicated below. Add rows, as needed.")
    software_vendor = models.TextField(blank=True, null=True)
    software_role = models.TextField(blank=True, null=True)

    merchants = models.ManyToManyField(Merchant)

    def __str__(self):
        return self.software_product
    class Meta:
        verbose_name_plural = "software"


class ServiceProvider(models.Model):
    service_provider_name = models.CharField(max_length=200, help_text="Service providers and other third parties with which the entity shares cardholder data")
    service_provider_data_shared = models.TextField(blank=True, null=True, help_text="What data is shared (for example, PAN, expiry date, etc.)")
    service_provider_sharing_purpose = models.TextField(blank=True, null=True, help_text="The purpose for sharing the data (for example, third-party storage, transaction processing, etc.)")
    service_provider_pci_status = models.TextField(blank=True, null=True, help_text="Status of PCI DSS Compliance (Date of AOC and version #)")

    merchants = models.ManyToManyField(Merchant)

    def __str__(self):
        return self.service_provider_name


class PaymentApplication(models.Model):
    payment_application_name = models.CharField(max_length=200, help_text="List all third-party payment application products and version numbers in use, including whether each payment application has been validated according to PA-DSS or PCI P2PE. Even if a payment application has been PA-DSS or PCI P2PE validated, the assessor still needs to verify that the application has been implemented in a PCI DSS compliant manner and environment, and according to the payment application vendor’s PA-DSS Implementation Guide for PA-DSS applications or P2PE Implementation Manual (PIM) and P2PE application vendor’s P2PE Application Implementation Guide for PCI P2PE applications/solutions.")
    payment_application_vendor = models.CharField(max_length=200, blank=True, null=True)
    payment_application_description = models.TextField(blank=True, null=True)
    payment_application_version = models.TextField(blank=True, null=True)
    payment_application_pa_dss_validation = models.BooleanField()
    payment_application_p2pe_validation = models.BooleanField()
    payment_application_listing_number = models.TextField(blank=True, null=True)
    payment_application_expire_date = models.DateTimeField(blank=True, null=True)

    merchants = models.ManyToManyField(Merchant)

    def __str__(self):
        return self.payment_application_name


class PaymentChannel(models.Model):
    payment_channel_type = models.CharField(max_length=200)

    merchants = models.ManyToManyField(Merchant, blank=True)

    def __str__(self):
        return self.payment_channel_type


class Requirement(models.Model):
    req_number = models.CharField(max_length=10)
    version = models.CharField(max_length=10, default='3.1')
    req_num_col1 = models.IntegerField(blank=True, null=True)
    req_num_col2 = models.IntegerField(blank=True, null=True)
    req_num_col3 = models.IntegerField(blank=True, null=True)
    req_num_col4 = models.IntegerField(blank=True, null=True)
    req_text_markdown = models.TextField()
    req_text = models.TextField(blank=True, default=' ')
    req_note_markdown = models.TextField(blank=True)
    req_note = models.TextField(blank=True)
    req_test_summ_markdown = models.TextField(blank=True)
    req_test_summ = models.TextField(blank=True)
    guidance_text_markdown = models.TextField(blank=True)
    guidance_text = models.TextField(blank=True)
    parent_req = models.ForeignKey( 'self', blank=True, null=True, related_name='child_req')
    req_descendants = models.IntegerField(blank=True, null=True, default=0)

    daily = 'Daily'
    weekly = 'Weekly'
    monthly = 'Monthly'
    quarterly = 'Quarterly'
    semiannually = 'Semiannually'
    annually = 'Annually'
    req_repeat_choices = (
        (daily,'Daily'),
        (weekly, 'Weekly'),
        (monthly, 'Monthly'),
        (quarterly, 'Quarterly'),
        (semiannually, 'Semiannually'),
        (annually, 'Annually'),
    )
    req_repeat_status =models.CharField(max_length=20,
                                          choices=req_repeat_choices,
                                          default=annually)
    expire_days = models.IntegerField(blank=True, null=True)

#    saq_a = 'A'
#    saq_aep = 'A-EP'
#    saq_b = 'B'
#    saq_c = 'C'
#    saq_cvt = 'C-VT'
#    saq_d = 'D'
#    saq_p2pe = 'P2PE'
#
#    saq_choices = (
#        (saq_a, 'SAQ A'),
#        (saq_aep, 'SAQ A-EP'),
#        (saq_b, 'SAQ B'),
#        (saq_c, 'SAQ C'),
#        (saq_cvt, 'SAQ C-VT'),
#        (saq_d, 'SAQ D'),
#        (saq_p2pe, 'SAQ P2PE'),
#    )
#    saq_req =models.CharField(max_length=4,
#                            choices=saq_choices,
#                            default=saq_d)

    saq_req = models.ForeignKey(SAQ, blank=True, null=True)

    def save(self, *args, **kwargs):

        r_text = markdown.markdown(self.req_text_markdown)
        r_text1 = str.replace(r_text,'<p>','<br />')
        r_text2 = str.replace(r_text1,'</p>','<br />')
        r_text3 = r_text2
        if r_text3.startswith('<br />'):
            r_text4 = r_text3[6:]
        else:
            r_text4 = r_text3
        if r_text4.endswith('<br />'):
            r_text5 = r_text4[:-6]
        else:
            r_text5 = r_text4
        self.req_text = r_text5

        r_note = markdown.markdown(self.req_note_markdown)
        r_note1 = str.replace(r_note,'<p>','<br />')
        r_note2 = str.replace(r_note1,'</p>','<br />')
        r_note3 = r_note2
        if r_note3.startswith('<br />'):
            r_note4 = r_note3[6:]
        else:
            r_note4 = r_note3
        if r_note4.endswith('<br />'):
            r_note5 = r_note4[:-6]
        else:
            r_note5 = r_note4
        self.req_note = r_note5

        r_test_summ = markdown.markdown(self.req_test_summ_markdown)
        r_test_summ1 = str.replace(r_test_summ,'<p>','<br />')
        r_test_summ2 = str.replace(r_test_summ1,'</p>','<br />')
        r_test_summ3 = r_test_summ2
        if r_test_summ3.startswith('<br />'):
            r_test_summ4 = r_test_summ3[6:]
        else:
            r_test_summ4 = r_test_summ3
        if r_test_summ4.endswith('<br />'):
            r_test_summ5 = r_test_summ4[:-6]
        else:
            r_test_summ5 = r_test_summ4
        self.req_test_summ = r_test_summ5

        r_guidance_text = markdown.markdown(self.guidance_text_markdown)
        r_guidance_text1 = str.replace(r_guidance_text,'<p>','<br />')
        r_guidance_text2 = str.replace(r_guidance_text1,'</p>','<br />')
        r_guidance_text3 = r_guidance_text2
        if r_guidance_text3.startswith('<br />'):
            r_guidance_text4 = r_guidance_text3[6:]
        else:
            r_guidance_text4 = r_guidance_text3
        if r_guidance_text4.endswith('<br />'):
            r_guidance_text5 = r_guidance_text4[:-6]
        else:
            r_guidance_text5 = r_guidance_text4
        self.guidance_text = r_guidance_text5


        rnum = self.req_number
        rd = Requirement.objects.filter(req_number__startswith=rnum+'.').filter(saq_req=self.saq_req).filter(version=self.version)
        self.req_descendants = rd.count() + 1

        if self.req_repeat_status == 'Daily':
            self.expire_days = 1
        elif self.req_repeat_status == 'Weekly':
            self.expire_days = 7
        elif self.req_repeat_status == 'Monthly':
            self.expire_days = 30
        elif self.req_repeat_status == 'Quarterly':
            self.expire_days = 90
        elif self.req_repeat_status == 'Semiannually':
            self.expire_days = 180
        else:
            self.expire_days = 365

        req_num_list = self.req_number.split('.')
        if len(req_num_list) > 0:
            try:
                rcol1 = int(req_num_list[0])
                self.req_num_col1 = rcol1
            except:
                self.req_num_col1 = 0
            if len(req_num_list) > 1:
                try:
                    rcol2 = int(req_num_list[1])
                    self.req_num_col2 = rcol2
                except:
                    self.req_num_col2 = 0
                if len(req_num_list) > 2:
                    try:
                        rcol3 = int(req_num_list[2])
                        self.req_num_col3 = rcol3
                    except:
                        self.req_num_col3 = 0
                    if len(req_num_list) > 3:
                        try:
                            rcol4 = int(req_num_list[3])
                            self.req_num_col4 = rcol4
                        except:
                            self.req_num_col4 = 0
                    else:
                        self.req_num_col4 = 0
                else:
                    self.req_num_col3 = 0
            else:
                self.req_num_col2 = 0
        else:
            self.req_num_col1 = 0

        super(Requirement, self).save(*args, **kwargs) # Call the "real" save() method.

    def req_name_number(self):

        return self.req_number + " " + self.req_text

    def __str__(self):
        return self.version + " " + self.saq_req.saq_name + " " + self.req_number

    class Meta:
        ordering = ["version", "saq_req",
                    "req_num_col1",
                    "req_num_col2", "req_num_col3", "req_num_col4", "req_number"]


class Testing_Procedure(models.Model):
    requirement = models.ForeignKey(Requirement)
    test_number = models.CharField(max_length=10)
    test_num_col1 = models.CharField(max_length=10, blank=True, null=True)
    test_num_col2 = models.CharField(max_length=10, blank=True, null=True)
    test_num_col3 = models.CharField(max_length=10, blank=True, null=True)
    test_num_col4 = models.CharField(max_length=10, blank=True, null=True)
    test_text_markdown = models.TextField()
    test_text = models.TextField(blank=True)
    reporting_instruction_markdown = models.TextField(blank=True)
    reporting_instruction = models.TextField(blank=True)

    def __str__(self):
        return self.test_number + " " + self.test_text

    def save(self, *args, **kwargs):
        t_text = markdown.markdown(self.test_text_markdown)
        t_text1 = str.replace(t_text,'<p>','<br />')
        t_text2 = str.replace(t_text1,'</p>','<br />')
        t_text3 = t_text2
        if t_text3.startswith('<br />'):
            t_text4 = t_text3[6:]
        else:
            t_text4 = t_text3
        if t_text4.endswith('<br />'):
            t_text5 = t_text4[:-6]
        else:
            t_text5 = t_text4
        self.test_text = t_text5

        r_inst = markdown.markdown(self.reporting_instruction_markdown)
        r_inst1 = str.replace(r_inst,'<p>','<br />')
        r_inst2 = str.replace(r_inst1,'</p>','<br />')
        r_inst3 = r_inst2
        if r_inst3.startswith('<br />'):
            r_inst4 = r_inst3[6:]
        else:
            r_inst4 = r_inst3
        if r_inst4.endswith('<br />'):
            r_inst5 = r_inst4[:-6]
        else:
            r_inst5 = r_inst4
        self.reporting_instruction = r_inst5


        test_num_list = self.test_number.split('.')
        if len(test_num_list) > 0:
            try:
                tcol1 = int(test_num_list[0])
                self.test_num_col1 = tcol1
            except:
                self.test_num_col1 = 0
            if len(test_num_list) > 1:
                try:
                    tcol2 = int(test_num_list[1])
                    self.test_num_col2 = tcol2
                except:
                    self.test_num_col2 = 0
                if len(test_num_list) > 2:
                    try:
                        tcol3 = int(test_num_list[2])
                        self.test_num_col3 = tcol3
                    except:
                        self.test_num_col3 = 0
                    if len(test_num_list) > 3:
                        try:
                            tcol4 = int(test_num_list[3])
                            self.test_num_col4 = tcol4
                        except:
                            self.test_num_col4 = 0
                    else:
                        self.test_num_col4 = 0
                else:
                    self.test_num_col3 = 0
            else:
                self.test_num_col2 = 0
        else:
            self.test_num_col1 = 0

        super(Testing_Procedure, self).save(*args, **kwargs) # Call the "real" save() method.

    class Meta:
        ordering = ["test_num_col1", "test_num_col2", "test_num_col3", "test_num_col4", "test_number"]


class Merch_Requirement(models.Model):
    requirement = models.ForeignKey(Requirement)
    merch_req_num = models.CharField(max_length=10, blank=True, null=True)
    merch_req_saq = models.CharField(max_length=4, blank=True, null=True)
    merch_req_num_col1 = models.IntegerField(blank=True, null=True)
    merch_req_num_col2 = models.IntegerField(blank=True, null=True)
    merch_req_num_col3 = models.IntegerField(blank=True, null=True)
    merch_req_num_col4 = models.IntegerField(blank=True, null=True)
    completion_date = models.DateTimeField('date completed', blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    merch_req_descendants = models.IntegerField(blank=True, null=True, default=0)
    merch_req_not_in_place = models.IntegerField(blank=True, null=True, default=0)
    merch_req_chi_status = models.IntegerField(blank=True, null=True, default=0)
    merch_req_chi_progress = models.IntegerField(blank=True, null=True, default=0)
    status_in_place = 'In Place'
    status_not_in_place = 'Not In Place'
    status_in_progress = 'In Progress'
    status_expired = 'Expired'
    status_na = 'Not Applicable'
    req_status_choices = (
        (status_in_place, 'In Place'),
        (status_not_in_place, 'Not In Place'),
        (status_in_progress, 'In Progress'),
        (status_expired, 'Expired'),
        (status_na, 'Not Applicable')

    )
    req_status =models.CharField(max_length=20,
                                          choices=req_status_choices,
                                          default=status_not_in_place)

#    saq_req = models.ForeignKey(SAQ, blank=True, null=True)


    merchant = models.ForeignKey(Merchant)

    def save(self, *args, **kwargs):
        self.merch_req_num = self.requirement.req_number
        self.merch_req_saq = str(self.requirement.saq_req.saq_name)
#        self.saq_req = self.requirement.saq_req
        self.merch_req_num_col1 = self.requirement.req_num_col1
        self.merch_req_num_col2 = self.requirement.req_num_col2
        self.merch_req_num_col3 = self.requirement.req_num_col3
        self.merch_req_num_col4 = self.requirement.req_num_col4
        self.merch_req_descendants = self.requirement.req_descendants

        if self.requirement.child_req is not None:
            r = self.requirement
            rnum = r.req_number
            merch_req = self
#            req_children = r.child_req.all()
#            merch_req_children = Merch_Requirement.objects.filter(requirement__in=req_children).filter(merchant=self.merchant)
            mer_req = Merch_Requirement.objects.filter(merch_req_num__startswith=rnum+'.').filter(merchant=self.merchant)
            chicount = mer_req.count()
            child_status = 0
            child_progress = 0
            for req in mer_req.all():
                if req.req_status == 'In Place':
                    child_status = child_status + 1
                    child_progress = child_progress + 1
                elif req.req_status == 'Not Applicable':
                    child_status = child_status + 1
                    child_progress = child_progress + 1
                elif req.req_status == 'In Progress':
                    child_progress = child_progress + 1


            try:
                test = Testing_Procedure.objects.filter(requirement=r)
            except:
                test = False

            try:
                find = Finding.objects.filter(merch_requirement=merch_req).latest('finding_date')
            except:
                find = False

            if test is False:
                if child_status == chicount:
                    merch_req.req_status = 'In Place'
                    child_status = child_status + 1
                    child_progress = child_progress + 1
                elif child_status > 0:
                    merch_req.req_status = 'In Progress'
                    child_progress = child_progress + 1
                elif child_status == 0 and child_progress > 0:
                    merch_req.req_status = 'In Progress'
                    child_progress = child_progress + 1
                else:
                    merch_req.req_status = 'Not In Place'
            else:
                if find is not False:
                    if child_status == chicount:
                        merch_req.req_status = find.req_status
                        if merch_req.req_status == 'In Place':
                            child_status = child_status + 1
                            child_progress = child_progress + 1
                    elif child_status > 0:
                        merch_req.req_status = 'In Progress'
                        child_progress = child_progress + 1
                    elif child_status == 0 and child_progress > 0:
                        merch_req.req_status = 'In Progress'
                        child_progress = child_progress + 1
                    else:
                        merch_req.req_status = 'Not In Place'
                else:
                    if child_status > 0:
                        merch_req.req_status = 'In Progress'
                        child_progress = child_progress + 1
                    elif child_status == 0 and child_progress > 0:
                        merch_req.req_status = 'In Progress'
                        child_progress = child_progress + 1
                    else:
                        merch_req.req_status = 'Not In Place'
            if child_progress > 1 and child_status == 0:
                merch_req.req_status = 'In Progress'
                child_progress = child_progress + 1
            self.merch_req_chi_status = child_status
            self.merch_req_chi_progress = child_progress - child_status
            self.merch_req_not_in_place = self.merch_req_descendants - self.merch_req_chi_status -self.merch_req_chi_progress

        else:
            r = self.requirement
            merch_req = self

            try:
                find = Finding.objects.filter(merch_requirement=merch_req).latest('finding_date')
            except:
                find = False

            if find is not False:
                merch_req.req_status = find.req_status
            else:
                merch_req.req_status = 'Not In Place'

        super(Merch_Requirement, self).save(*args, **kwargs) # Call the "real" save() method.
        if self.requirement.parent_req is not None:
            p = self.requirement.parent_req
            rnum = p.req_number
            merch_par = Merch_Requirement.objects.get(requirement=p, merchant=self.merchant)
#            par_req_children = p.child_req.all()
#            merch_par_req_children = Merch_Requirement.objects.filter(requirement__in=par_req_children).filter(merchant=self.merchant)
            mer_req = Merch_Requirement.objects.filter(merch_req_num__startswith=rnum+'.').filter(merchant=self.merchant)
            chicount = mer_req.count()
            child_status = 0
            child_progress = 0
            for req in mer_req.all():
                if req.req_status == 'In Place':
                    child_status = child_status + 1
                    child_progress = child_progress + 1
                elif req.req_status == 'Not Applicable':
                    child_status = child_status + 1
                    child_progress = child_progress + 1
                elif req.req_status == 'In Progress':
                    child_progress = child_progress + 1
            merch_par.merch_req_chi_status = child_status
            merch_par.merch_req_chi_progress = child_progress

            try:
                test = Testing_Procedure.objects.filter(requirement=p)
            except:
                test = False

            if child_status == chicount:
                if test is False:
                    merch_par.req_status = 'In Place'
                    merch_par.merch_req_chi_status = child_status + 1
                    merch_par.merch_req_chi_progress = child_progress + 1
                else:
                    merch_par.req_status = 'In Progress'
                    merch_par.merch_req_chi_progress = child_progress + 1
            elif merch_par.merch_req_chi_status > 0:
                merch_par.req_status = 'In Progress'
                merch_par.merch_req_chi_progress = child_progress + 1
            elif merch_par.merch_req_chi_progress > 0:
                merch_par.req_status = 'In Progress'
                merch_par.merch_req_chi_progress = child_progress + 1
            else:
                merch_par.req_status = 'Not In Place'

            merch_par.save()
        else:
            m = self.merchant
            p = self.requirement.parent_req

            total_req = m.merch_requirement_set.count()
            req_complete = 0

            for req in m.merch_requirement_set.all():
                if req.req_status == 'In Place':
                    req_complete = req_complete + 1
                elif req.req_status == 'Not Applicable':
                    req_complete = req_complete + 1
            req_percent = req_complete / total_req
            m.merch_percent = req_percent * 100
            m.total_req = total_req
            m.req_complete = req_complete
            m.save()

    def req_name_number(self):

        return self.requirement.req_number + " " + self.requirement.req_text

    def __str__(self):
        return self.merchant.merchant_name + " " + self.requirement.req_number

    class Meta:
        ordering = [
            "merch_req_num_col1",
            "merch_req_num_col2", "merch_req_num_col3", "merch_req_num_col4", "requirement"]


class Finding(models.Model):
    merch_requirement = models.ForeignKey(Merch_Requirement, blank=True, null=True)
    finding_date = models.DateTimeField('date entered')
    finding_text = models.TextField()
    req_status = models.CharField(max_length=20, blank=True, null=True)
    user = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Finding, self).save(*args, **kwargs) # Call the "real" save() method.
        finding_req = self.merch_requirement
        finding_req.save()
        if finding_req.req_status == finding_req.status_in_place:
            finding_req.expire_date = self.finding_date + timedelta(days=finding_req.requirement.expire_days)
            finding_req.completion_date = self.finding_date
        else:
            finding_req.expire_date = None
            finding_req.completion_date = None

        finding_req.save()

    def __str__(self):
        return self.finding_text
