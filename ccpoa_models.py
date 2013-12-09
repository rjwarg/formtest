# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class GlCollate(models.Model):
    class Meta:
        db_table = ' GL_COLLATE'

class GlCtype(models.Model):
    class Meta:
        db_table = ' GL_CTYPE'

class Version(models.Model):
    class Meta:
        db_table = ' VERSION'

class Agycode(models.Model):
    agy_code = models.CharField(max_length=3, blank=True)
    facility = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'agycode'

class Aljs(models.Model):
    aljcode = models.CharField(max_length=3, blank=True)
    aljdesc = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'aljs'

class Appren(models.Model):
    app_no = models.IntegerField(null=True, blank=True)
    assn = models.CharField(max_length=11, blank=True)
    lstupdate = models.DateField(null=True, blank=True)
    apromo = models.CharField(max_length=1, blank=True)
    aholdrs = models.CharField(max_length=6, blank=True)
    acolhrs = models.CharField(max_length=6, blank=True)
    abene = models.CharField(max_length=1, blank=True)
    amocred = models.CharField(max_length=1, blank=True)
    agrade = models.CharField(max_length=2, blank=True)
    abillhrs = models.CharField(max_length=6, blank=True)
    acomphrs = models.CharField(max_length=6, blank=True)
    agrand = models.CharField(max_length=1, blank=True)
    aactive = models.CharField(max_length=1, blank=True)
    ahrsdat = models.DateField(null=True, blank=True)
    ahiredat = models.DateField(null=True, blank=True)
    avet = models.CharField(max_length=1, blank=True)
    axpthrs = models.CharField(max_length=6, blank=True)
    csex = models.CharField(max_length=1, blank=True)
    crace = models.CharField(max_length=1, blank=True)
    cupdat = models.DateField(null=True, blank=True)
    crep = models.CharField(max_length=1, blank=True)
    cflag = models.CharField(max_length=40, blank=True)
    cakey = models.CharField(max_length=1, blank=True)
    inactdat = models.DateField(null=True, blank=True)
    reactdat = models.DateField(null=True, blank=True)
    stype = models.CharField(max_length=1, blank=True)
    sclass = models.CharField(max_length=6, blank=True)
    ssection = models.CharField(max_length=10, blank=True)
    scrscode = models.IntegerField(null=True, blank=True)
    scourse = models.CharField(max_length=10, blank=True)
    syrs = models.CharField(max_length=2, blank=True)
    sreqhrs = models.CharField(max_length=6, blank=True)
    startdate = models.DateField(null=True, blank=True)
    shours = models.CharField(max_length=6, blank=True)
    shoursbill = models.CharField(max_length=6, blank=True)
    sactive = models.CharField(max_length=1, blank=True)
    srs = models.CharField(max_length=6, blank=True)
    sholdhrs = models.CharField(max_length=6, blank=True)
    a1 = models.IntegerField(null=True, blank=True)
    a2 = models.IntegerField(null=True, blank=True)
    a3 = models.IntegerField(null=True, blank=True)
    a4 = models.IntegerField(null=True, blank=True)
    a5 = models.IntegerField(null=True, blank=True)
    a6 = models.IntegerField(null=True, blank=True)
    a7 = models.IntegerField(null=True, blank=True)
    a8 = models.IntegerField(null=True, blank=True)
    a9 = models.IntegerField(null=True, blank=True)
    a10 = models.IntegerField(null=True, blank=True)
    a11 = models.IntegerField(null=True, blank=True)
    a12 = models.IntegerField(null=True, blank=True)
    a13 = models.IntegerField(null=True, blank=True)
    a14 = models.IntegerField(null=True, blank=True)
    a15 = models.IntegerField(null=True, blank=True)
    a16 = models.IntegerField(null=True, blank=True)
    b1 = models.IntegerField(null=True, blank=True)
    b2 = models.IntegerField(null=True, blank=True)
    b3 = models.IntegerField(null=True, blank=True)
    b4 = models.IntegerField(null=True, blank=True)
    b5 = models.IntegerField(null=True, blank=True)
    b6 = models.IntegerField(null=True, blank=True)
    b7 = models.IntegerField(null=True, blank=True)
    b8 = models.IntegerField(null=True, blank=True)
    b9 = models.IntegerField(null=True, blank=True)
    b10 = models.IntegerField(null=True, blank=True)
    b11 = models.IntegerField(null=True, blank=True)
    b12 = models.IntegerField(null=True, blank=True)
    b13 = models.IntegerField(null=True, blank=True)
    b14 = models.IntegerField(null=True, blank=True)
    b15 = models.IntegerField(null=True, blank=True)
    b16 = models.IntegerField(null=True, blank=True)
    c1 = models.IntegerField(null=True, blank=True)
    c2 = models.IntegerField(null=True, blank=True)
    c3 = models.IntegerField(null=True, blank=True)
    c4 = models.IntegerField(null=True, blank=True)
    c5 = models.IntegerField(null=True, blank=True)
    c6 = models.IntegerField(null=True, blank=True)
    c7 = models.IntegerField(null=True, blank=True)
    c8 = models.IntegerField(null=True, blank=True)
    c9 = models.IntegerField(null=True, blank=True)
    c10 = models.IntegerField(null=True, blank=True)
    c11 = models.IntegerField(null=True, blank=True)
    c12 = models.IntegerField(null=True, blank=True)
    c13 = models.IntegerField(null=True, blank=True)
    c14 = models.IntegerField(null=True, blank=True)
    c15 = models.IntegerField(null=True, blank=True)
    c16 = models.IntegerField(null=True, blank=True)
    d1 = models.IntegerField(null=True, blank=True)
    d2 = models.IntegerField(null=True, blank=True)
    d3 = models.IntegerField(null=True, blank=True)
    d4 = models.IntegerField(null=True, blank=True)
    d5 = models.IntegerField(null=True, blank=True)
    d6 = models.IntegerField(null=True, blank=True)
    d7 = models.IntegerField(null=True, blank=True)
    d8 = models.IntegerField(null=True, blank=True)
    d9 = models.IntegerField(null=True, blank=True)
    d10 = models.IntegerField(null=True, blank=True)
    d11 = models.IntegerField(null=True, blank=True)
    d12 = models.IntegerField(null=True, blank=True)
    d13 = models.IntegerField(null=True, blank=True)
    d14 = models.IntegerField(null=True, blank=True)
    d15 = models.IntegerField(null=True, blank=True)
    d16 = models.IntegerField(null=True, blank=True)
    e1 = models.IntegerField(null=True, blank=True)
    e2 = models.IntegerField(null=True, blank=True)
    e3 = models.IntegerField(null=True, blank=True)
    e4 = models.IntegerField(null=True, blank=True)
    e5 = models.IntegerField(null=True, blank=True)
    e6 = models.IntegerField(null=True, blank=True)
    e7 = models.IntegerField(null=True, blank=True)
    e8 = models.IntegerField(null=True, blank=True)
    e9 = models.IntegerField(null=True, blank=True)
    e10 = models.IntegerField(null=True, blank=True)
    e11 = models.IntegerField(null=True, blank=True)
    e12 = models.IntegerField(null=True, blank=True)
    e13 = models.IntegerField(null=True, blank=True)
    e14 = models.IntegerField(null=True, blank=True)
    e15 = models.IntegerField(null=True, blank=True)
    e16 = models.IntegerField(null=True, blank=True)
    e17 = models.IntegerField(null=True, blank=True)
    e18 = models.IntegerField(null=True, blank=True)
    e19 = models.IntegerField(null=True, blank=True)
    e20 = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'appren'

class Arb(models.Model):
    aid_no = models.IntegerField(null=True, blank=True)
    sacdt = models.DateField(null=True, blank=True)
    stardt = models.DateField(null=True, blank=True)
    srcdt = models.DateField(null=True, blank=True)
    tidate1 = models.DateField(null=True, blank=True)
    tinit1 = models.CharField(max_length=4, blank=True)
    tinit2 = models.CharField(max_length=4, blank=True)
    tinit3 = models.CharField(max_length=4, blank=True)
    tidate2 = models.DateField(null=True, blank=True)
    tidate3 = models.DateField(null=True, blank=True)
    ty1 = models.CharField(max_length=1, blank=True)
    tn1 = models.CharField(max_length=1, blank=True)
    ty2 = models.CharField(max_length=1, blank=True)
    tn2 = models.CharField(max_length=1, blank=True)
    ty3 = models.CharField(max_length=1, blank=True)
    tn3 = models.CharField(max_length=1, blank=True)
    tdate4 = models.DateField(null=True, blank=True)
    reserch = models.CharField(max_length=10, blank=True)
    rdate1 = models.DateField(null=True, blank=True)
    rdate2 = models.DateField(null=True, blank=True)
    rdate3 = models.DateField(null=True, blank=True)
    rdate4 = models.DateField(null=True, blank=True)
    ldate1 = models.DateField(null=True, blank=True)
    strdt1 = models.DateField(null=True, blank=True)
    strdt2 = models.DateField(null=True, blank=True)
    strdt3 = models.DateField(null=True, blank=True)
    strdt4 = models.DateField(null=True, blank=True)
    frdt1 = models.DateField(null=True, blank=True)
    frdt2 = models.DateField(null=True, blank=True)
    arbdt1 = models.DateField(null=True, blank=True)
    stdate = models.DateField(null=True, blank=True)
    approve = models.CharField(max_length=1, blank=True)
    agsec = models.IntegerField(null=True, blank=True)
    agid_no = models.FloatField(null=True, blank=True)
    meritdt = models.DateField(null=True, blank=True)
    waddell = models.DateField(null=True, blank=True)
    briefdt = models.DateField(null=True, blank=True)
    aaadt = models.DateField(null=True, blank=True)
    demanddt = models.DateField(null=True, blank=True)
    fourthdue = models.DateField(null=True, blank=True)
    asub = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'arb'

class Arbhearing(models.Model):
    ahid_no = models.IntegerField()
    ah_join = models.IntegerField()
    ahdate = models.DateField()
    ahtime = models.CharField(max_length=7, blank=True)
    ahplac = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'arbhearing'

class Arbit(models.Model):
    aname = models.CharField(max_length=30, blank=True)
    afirstname = models.CharField(max_length=20, blank=True)
    aaddress = models.CharField(max_length=30, blank=True)
    acity = models.CharField(max_length=20, blank=True)
    astate = models.CharField(max_length=2, blank=True)
    azip = models.CharField(max_length=10, blank=True)
    aphone = models.CharField(max_length=13, blank=True)
    ajoincde = models.CharField(max_length=5, blank=True)
    afax = models.CharField(max_length=13, blank=True)
    aemail = models.CharField(max_length=50, blank=True)
    afees = models.CharField(max_length=20, blank=True)
    atitle = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'arbit'

class Assessment(models.Model):
    artype = models.CharField(max_length=1, blank=True)
    asocial = models.CharField(max_length=11)
    afname = models.CharField(max_length=1, blank=True)
    aminitial = models.CharField(max_length=1, blank=True)
    alname = models.CharField(max_length=13, blank=True)
    aagency = models.CharField(max_length=3, blank=True)
    arunit = models.CharField(max_length=3, blank=True)
    atotprem = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    apptype = models.CharField(max_length=1, blank=True)
    admo = models.CharField(max_length=2, blank=True)
    adyr = models.CharField(max_length=4, blank=True)
    adedcode = models.CharField(max_length=3, blank=True)
    aorgcode = models.CharField(max_length=3, blank=True)
    adedamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    awarrantno = models.IntegerField(null=True, blank=True)
    aformat = models.CharField(max_length=1, blank=True)
    aflex = models.CharField(max_length=1, blank=True)
    afilecode = models.CharField(max_length=3, blank=True)
    asortru = models.CharField(max_length=3, blank=True)
    ashamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    class Meta:
        db_table = 'assessment'

class Assgn(models.Model):
    case = models.CharField(max_length=10, blank=True)
    nm = models.CharField(max_length=20, blank=True)
    penalty = models.CharField(max_length=10, blank=True)
    dateh = models.DateField(null=True, blank=True)
    datec = models.CharField(max_length=8, blank=True)
    staff = models.CharField(max_length=3, blank=True)
    instc = models.CharField(max_length=7, blank=True)
    done = models.CharField(max_length=1, blank=True)
    dateassn = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'assgn'

class Assign(models.Model):
    assid_no = models.IntegerField()
    rep = models.CharField(max_length=3)
    assdt = models.DateField()
    asscd = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'assign'

class Assigng(models.Model):
    assidg_no = models.IntegerField()
    repg = models.CharField(max_length=3)
    assdtg = models.DateField()
    asscde = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'assigng'

class AuditLog(models.Model):
    id = models.IntegerField()
    filenuma = models.TextField()
    date_time = models.DateTimeField()
    sql = models.TextField()
    fullname = models.TextField()
    class Meta:
        db_table = 'audit_log'

class Ballotcde(models.Model):
    ballot_code = models.CharField(max_length=3, blank=True)
    ballot_desc = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'ballotcde'

class Breb(models.Model):
    breb_no = models.IntegerField()
    blegal_no = models.FloatField(null=True, blank=True)
    brebdt = models.DateField(null=True, blank=True)
    brebnum = models.FloatField(null=True, blank=True)
    numx = models.CharField(max_length=2, blank=True)
    bname = models.CharField(max_length=30, blank=True)
    bname1 = models.CharField(max_length=30, blank=True)
    bname2 = models.CharField(max_length=30, blank=True)
    binst = models.CharField(max_length=7, blank=True)
    bclosedt = models.DateField(null=True, blank=True)
    bcomment = models.CharField(max_length=100, blank=True)
    bnote = models.CharField(max_length=100, blank=True)
    btype = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'breb'

class Bulkmailqueries(models.Model):
    pri_key = models.IntegerField()
    group_name = models.TextField()
    where_clause = models.TextField(blank=True)
    class Meta:
        db_table = 'bulkmailqueries'

class Bxref(models.Model):
    xbreb_no = models.IntegerField(null=True, blank=True)
    xpar_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'bxref'

class Category(models.Model):
    id = models.IntegerField()
    active = models.IntegerField()
    category_name = models.TextField()
    class Meta:
        db_table = 'category'

class Ccjc(models.Model):
    zip = models.CharField(max_length=10, blank=True)
    state1 = models.CharField(max_length=20)
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    title = models.CharField(max_length=20, blank=True)
    union = models.CharField(max_length=34, blank=True)
    street = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=20, blank=True)
    state2 = models.CharField(max_length=2, blank=True)
    work = models.CharField(max_length=13, blank=True)
    home = models.CharField(max_length=13, blank=True)
    notes = models.CharField(max_length=60, blank=True)
    o_o = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'ccjc'

class ChangeLog(models.Model):
    record_id = models.IntegerField()
    requestor = models.CharField(max_length=50, blank=True)
    user = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField()
    affected_table = models.CharField(max_length=30, blank=True)
    pre_change_data = models.CharField(max_length=2000)
    post_change_data = models.CharField(max_length=2000, blank=True)
    class Meta:
        db_table = 'change_log'

class Chaptercal(models.Model):
    chcalid_no = models.IntegerField()
    chcal_join = models.IntegerField()
    chcaldate = models.DateField()
    chcaltime = models.CharField(max_length=7)
    chcalplac = models.CharField(max_length=50)
    chcaladdr = models.CharField(max_length=50)
    chcalfrep = models.CharField(max_length=3)
    chcalnote = models.TextField(blank=True)
    class Meta:
        db_table = 'chaptercal'

class Chapters(models.Model):
    chapid_no = models.IntegerField()
    chap_join = models.CharField(max_length=3, blank=True)
    chap_abbr = models.CharField(max_length=25, blank=True)
    class Meta:
        db_table = 'chapters'

class Coassign(models.Model):
    coassid_no = models.IntegerField()
    coassjoin = models.IntegerField()
    corep = models.CharField(max_length=3)
    coassdt = models.DateField(null=True, blank=True)
    coasscd = models.CharField(max_length=1)
    cofilenum = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'coassign'

class Commini(models.Model):
    cmid_no = models.IntegerField()
    comone = models.CharField(max_length=250, blank=True)
    class Meta:
        db_table = 'commini'

class CompDed(models.Model):
    ssn = models.CharField(max_length=11, blank=True)
    f_int = models.CharField(max_length=1, blank=True)
    m_int = models.CharField(max_length=1, blank=True)
    surname = models.CharField(max_length=13, blank=True)
    period_m = models.SmallIntegerField(null=True, blank=True)
    period_y = models.SmallIntegerField(null=True, blank=True)
    ded_code = models.CharField(max_length=3, blank=True)
    org_code = models.CharField(max_length=3, blank=True)
    t_ded = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    credit = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'comp_ded'

class Conmou(models.Model):
    csid_no = models.CharField(max_length=12)
    scdesc = models.CharField(max_length=50)
    class Meta:
        db_table = 'conmou'

class Contract(models.Model):
    safety = models.CharField(max_length=2, blank=True)
    training = models.CharField(max_length=2, blank=True)
    overcrowd = models.CharField(max_length=2, blank=True)
    benefits = models.CharField(max_length=2, blank=True)
    salary = models.CharField(max_length=2, blank=True)
    aids = models.CharField(max_length=2, blank=True)
    promotion = models.CharField(max_length=2, blank=True)
    seniority = models.CharField(max_length=2, blank=True)
    cpobor = models.CharField(max_length=2, blank=True)
    multi = models.CharField(max_length=2, blank=True)
    retire = models.CharField(max_length=2, blank=True)
    other = models.CharField(max_length=2, blank=True)
    other1 = models.CharField(max_length=30, blank=True)
    other2 = models.CharField(max_length=2, blank=True)
    other3 = models.CharField(max_length=2, blank=True)
    other4 = models.CharField(max_length=2, blank=True)
    other5 = models.CharField(max_length=2, blank=True)
    other6 = models.CharField(max_length=2, blank=True)
    other7 = models.CharField(max_length=2, blank=True)
    other8 = models.CharField(max_length=2, blank=True)
    other9 = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = 'contract'

class Contrep(models.Model):
    rcont1 = models.CharField(max_length=2, blank=True)
    rcont2 = models.CharField(max_length=2, blank=True)
    rcont3 = models.CharField(max_length=2, blank=True)
    rcont4 = models.CharField(max_length=2, blank=True)
    rcont5 = models.CharField(max_length=2, blank=True)
    rcont6 = models.CharField(max_length=2, blank=True)
    rcont7 = models.CharField(max_length=2, blank=True)
    rcont8 = models.CharField(max_length=2, blank=True)
    rcont9 = models.CharField(max_length=2, blank=True)
    rcont10 = models.CharField(max_length=2, blank=True)
    rcont11 = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'contrep'

class ConvMaster(models.Model):
    cid_no = models.IntegerField()
    c_ssn = models.CharField(max_length=11)
    cfirst_name = models.CharField(max_length=20, blank=True)
    cname = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=20, blank=True)
    czip = models.CharField(max_length=10, blank=True)
    dob = models.DateField(null=True, blank=True)
    hphone = models.CharField(max_length=13, blank=True)
    cstat = models.CharField(max_length=1)
    cupdate = models.DateField(null=True, blank=True)
    cemail = models.CharField(max_length=25, blank=True)
    cpmb = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'conv_master'

class County(models.Model):
    coid_no = models.IntegerField()
    cozip = models.CharField(max_length=5, blank=True)
    county = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'county'

class Course(models.Model):
    course_id = models.IntegerField()
    course_txt = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'course'

class Curcode(models.Model):
    ccode = models.CharField(max_length=3, blank=True)
    cdesc = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = 'curcode'

class Cusa(models.Model):
    crtype = models.CharField(max_length=1, blank=True)
    csocial = models.CharField(max_length=11)
    cfname = models.CharField(max_length=1, blank=True)
    cminitial = models.CharField(max_length=1, blank=True)
    clname = models.CharField(max_length=13, blank=True)
    cagency = models.CharField(max_length=3, blank=True)
    crunit = models.CharField(max_length=3, blank=True)
    ctotprem = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    cpptype = models.CharField(max_length=1, blank=True)
    cdmo = models.CharField(max_length=2, blank=True)
    cdyr = models.CharField(max_length=4, blank=True)
    cdedcode = models.CharField(max_length=3, blank=True)
    corgcode = models.CharField(max_length=3, blank=True)
    cdedamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    cwarrantno = models.IntegerField(null=True, blank=True)
    cformat = models.CharField(max_length=1, blank=True)
    cflex = models.CharField(max_length=1, blank=True)
    cfilecode = models.CharField(max_length=3, blank=True)
    csortru = models.CharField(max_length=3, blank=True)
    cshamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    class Meta:
        db_table = 'cusa'

class Deccodes(models.Model):
    dcode = models.CharField(max_length=3)
    ddesc = models.CharField(max_length=40)
    class Meta:
        db_table = 'deccodes'

class Deduction(models.Model):
    rtype = models.CharField(max_length=1, blank=True)
    social = models.CharField(max_length=11)
    fname = models.CharField(max_length=1, blank=True)
    minitial = models.CharField(max_length=1, blank=True)
    lname = models.CharField(max_length=13, blank=True)
    agency = models.CharField(max_length=3, blank=True)
    runit = models.CharField(max_length=3, blank=True)
    totprem = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    pptype = models.CharField(max_length=1, blank=True)
    dmo = models.CharField(max_length=2, blank=True)
    dyr = models.CharField(max_length=4, blank=True)
    dedcode = models.CharField(max_length=3, blank=True)
    orgcode = models.CharField(max_length=3, blank=True)
    dedamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    warrantno = models.IntegerField(null=True, blank=True)
    format = models.CharField(max_length=1, blank=True)
    flex = models.CharField(max_length=1, blank=True)
    filecode = models.CharField(max_length=3, blank=True)
    sortru = models.CharField(max_length=3, blank=True)
    shamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    class Meta:
        db_table = 'deduction'

class Department(models.Model):
    deptcode = models.CharField(max_length=3)
    deptdesc = models.TextField()
    class Meta:
        db_table = 'department'

class Eevent(models.Model):
    eeid_no = models.IntegerField()
    eerep = models.CharField(max_length=3)
    eemail = models.CharField(max_length=50, blank=True)
    eereport = models.CharField(max_length=50)
    eenterval = models.CharField(max_length=1)
    class Meta:
        db_table = 'eevent'

class Emailer(models.Model):
    lastname = models.CharField(max_length=21, blank=True)
    firstname = models.CharField(max_length=21, blank=True)
    address = models.CharField(max_length=35, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    homephone = models.CharField(max_length=13, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    ranksup = models.CharField(max_length=1, blank=True)
    institution = models.CharField(max_length=7, blank=True)
    status = models.CharField(max_length=1, blank=True)
    reason = models.IntegerField(null=True, blank=True)
    jobtitle = models.IntegerField(null=True, blank=True)
    boardmember = models.CharField(max_length=1, blank=True)
    pie = models.CharField(max_length=1, blank=True)
    id_no = models.IntegerField(null=True, blank=True)
    zipext = models.CharField(max_length=4, blank=True)
    pmb = models.CharField(max_length=13, blank=True)
    email = models.CharField(max_length=50, blank=True)
    oboard = models.CharField(max_length=1, blank=True)
    ochaprs = models.CharField(max_length=1, blank=True)
    oexec = models.CharField(max_length=1, blank=True)
    workphone = models.CharField(max_length=13, blank=True)
    ccpoaphone = models.CharField(max_length=13, blank=True)
    ojs = models.CharField(max_length=1, blank=True)
    ocjs = models.CharField(max_length=1, blank=True)
    cellphone = models.CharField(max_length=13, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = 'emailer'

class Employee(models.Model):
    empid_no = models.IntegerField()
    emp_ssn = models.CharField(max_length=9)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=35, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=50)
    startdate = models.DateField()
    department = models.CharField(max_length=20)
    class Meta:
        db_table = 'employee'

class Errorcode(models.Model):
    error_number = models.IntegerField()
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'errorcode'

class Errorlog(models.Model):
    id_no = models.IntegerField()
    timestamp = models.DateTimeField(null=True, blank=True)
    process_name = models.TextField(blank=True)
    error_number = models.IntegerField(null=True, blank=True)
    error_desc = models.TextField(blank=True)
    raw_data = models.TextField(blank=True) # This field type is a guess.
    status = models.TextField(blank=True)
    class Meta:
        db_table = 'errorlog'

class Exec(models.Model):
    exno_id = models.IntegerField()
    exec_no = models.IntegerField(null=True, blank=True)
    exectype = models.CharField(max_length=2)
    filenume = models.IntegerField()
    subnume = models.IntegerField()
    subexte = models.IntegerField()
    execrep = models.CharField(max_length=3)
    execdte = models.DateField()
    extitle = models.CharField(max_length=35, blank=True)
    extitl2 = models.CharField(max_length=35, blank=True)
    extitl3 = models.CharField(max_length=35, blank=True)
    exnotes = models.TextField(blank=True)
    exdeddt = models.DateField(null=True, blank=True)
    exinst = models.CharField(max_length=7, blank=True)
    class Meta:
        db_table = 'exec'

class Filetypes(models.Model):
    fid_no = models.IntegerField()
    ftcode = models.CharField(max_length=2)
    ftdesc = models.CharField(max_length=35)
    class Meta:
        db_table = 'filetypes'

class Finalcode(models.Model):
    fcode = models.CharField(max_length=3)
    fdesc = models.CharField(max_length=40)
    class Meta:
        db_table = 'finalcode'

class Flsaq(models.Model):
    flsaqid_no = models.IntegerField()
    flsaq_join = models.IntegerField(null=True, blank=True)
    flsaq_date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'flsaq'

class Frepchapters(models.Model):
    frchid_no = models.IntegerField()
    frch_join = models.CharField(max_length=3, blank=True)
    frch_chap = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'frepchapters'

class Fsla(models.Model):
    fsla_no = models.CharField(max_length=11, blank=True)
    fsladate = models.DateField(null=True, blank=True)
    fslastat = models.CharField(max_length=2, blank=True)
    fslasuit = models.CharField(max_length=15, blank=True)
    fslatdy = models.DateField(null=True, blank=True)
    fslan1 = models.CharField(max_length=60, blank=True)
    fslan2 = models.CharField(max_length=60, blank=True)
    fslan3 = models.CharField(max_length=60, blank=True)
    fslap = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'fsla'

class Garb(models.Model):
    gaid_no = models.IntegerField(null=True, blank=True)
    gsacdt = models.DateField(null=True, blank=True)
    gstardt = models.DateField(null=True, blank=True)
    gsrcdt = models.DateField(null=True, blank=True)
    gtidate1 = models.DateField(null=True, blank=True)
    gtinit1 = models.CharField(max_length=4, blank=True)
    gtinit2 = models.CharField(max_length=4, blank=True)
    gtinit3 = models.CharField(max_length=4, blank=True)
    gtidate2 = models.DateField(null=True, blank=True)
    gtidate3 = models.DateField(null=True, blank=True)
    gty1 = models.CharField(max_length=1, blank=True)
    gtn1 = models.CharField(max_length=1, blank=True)
    gty2 = models.CharField(max_length=1, blank=True)
    gtn2 = models.CharField(max_length=1, blank=True)
    gty3 = models.CharField(max_length=1, blank=True)
    gtn3 = models.CharField(max_length=1, blank=True)
    gtdate4 = models.DateField(null=True, blank=True)
    greserch = models.CharField(max_length=10, blank=True)
    grdate1 = models.DateField(null=True, blank=True)
    grdate2 = models.DateField(null=True, blank=True)
    grdate3 = models.DateField(null=True, blank=True)
    grdate4 = models.DateField(null=True, blank=True)
    gldate1 = models.DateField(null=True, blank=True)
    gstrdt1 = models.DateField(null=True, blank=True)
    gstrdt2 = models.DateField(null=True, blank=True)
    gstrdt3 = models.DateField(null=True, blank=True)
    gstrdt4 = models.DateField(null=True, blank=True)
    gfrdt1 = models.DateField(null=True, blank=True)
    gfrdt2 = models.DateField(null=True, blank=True)
    garbdt1 = models.DateField(null=True, blank=True)
    gstdate = models.DateField(null=True, blank=True)
    gapprove = models.CharField(max_length=1, blank=True)
    gagsec = models.IntegerField(null=True, blank=True)
    gagid_no = models.FloatField(null=True, blank=True)
    gmeritdt = models.DateField(null=True, blank=True)
    gwaddell = models.DateField(null=True, blank=True)
    gbriefdt = models.DateField(null=True, blank=True)
    gaaadt = models.DateField(null=True, blank=True)
    gdemanddt = models.DateField(null=True, blank=True)
    gfourthdue = models.DateField(null=True, blank=True)
    gresult = models.CharField(max_length=100, blank=True)
    gassigned = models.CharField(max_length=30, blank=True)
    gsub = models.CharField(max_length=1, blank=True)
    agkey = models.CharField(max_length=12, blank=True)
    gmeritdec = models.DateField(null=True, blank=True)
    gsrcdec = models.DateField(null=True, blank=True)
    gfinal = models.CharField(max_length=3, blank=True)
    gsrcresult = models.CharField(max_length=3, blank=True)
    mdte = models.DateField(null=True, blank=True)
    mccporep = models.CharField(max_length=3, blank=True)
    mstrep = models.CharField(max_length=20, blank=True)
    marbit = models.CharField(max_length=20, blank=True)
    mdecide = models.DateField(null=True, blank=True)
    mdecide2 = models.CharField(max_length=3, blank=True)
    mcomment = models.CharField(max_length=20, blank=True)
    mcomment2 = models.CharField(max_length=20, blank=True)
    acode = models.CharField(max_length=5, blank=True)
    gmrevdue = models.DateField(null=True, blank=True)
    grevccde = models.CharField(max_length=3, blank=True)
    grevecom = models.CharField(max_length=80, blank=True)
    gsrcdue = models.DateField(null=True, blank=True)
    gsrcccde = models.CharField(max_length=3, blank=True)
    gsrccom = models.CharField(max_length=80, blank=True)
    grdate5 = models.DateField(null=True, blank=True)
    grdate6 = models.DateField(null=True, blank=True)
    grdate7 = models.DateField(null=True, blank=True)
    grdate8 = models.DateField(null=True, blank=True)
    garbseldue = models.DateField(null=True, blank=True)
    gdemanddt2 = models.DateField(null=True, blank=True)
    gconsol = models.DateField(null=True, blank=True)
    garbsubdue = models.DateField(null=True, blank=True)
    gdecrec = models.DateField(null=True, blank=True)
    gsumdue = models.DateField(null=True, blank=True)
    gsetpendte = models.DateField(null=True, blank=True)
    gsettickle = models.DateField(null=True, blank=True)
    gpetconf = models.CharField(max_length=3, blank=True)
    gjursret = models.CharField(max_length=3, blank=True)
    gcrossref = models.CharField(max_length=20, blank=True)
    gcbriefrec = models.DateField(null=True, blank=True)
    gsbriefrec = models.DateField(null=True, blank=True)
    gcurstat = models.CharField(max_length=150, blank=True)
    garbdte2 = models.DateField(null=True, blank=True)
    garbdte3 = models.DateField(null=True, blank=True)
    garbdte4 = models.DateField(null=True, blank=True)
    garbdte5 = models.DateField(null=True, blank=True)
    garbdte6 = models.DateField(null=True, blank=True)
    garbdte7 = models.DateField(null=True, blank=True)
    garbdte8 = models.DateField(null=True, blank=True)
    garbdte9 = models.DateField(null=True, blank=True)
    total_cost = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    ccpoa_cost = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    marrechq = models.DateField(null=True, blank=True)
    lmemcomp = models.DateField(null=True, blank=True)
    clientltr = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'garb'

class Gc(models.Model):
    gckey = models.CharField(max_length=12)
    gctext = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'gc'

class Grev(models.Model):
    grec_no = models.IntegerField()
    gmem_no = models.IntegerField(null=True, blank=True)
    filetypeg = models.CharField(max_length=2, blank=True)
    filenumg = models.IntegerField(null=True, blank=True)
    grevext = models.IntegerField(null=True, blank=True)
    lglfilenum = models.IntegerField(null=True, blank=True)
    filedate = models.DateField(null=True, blank=True)
    contyr = models.CharField(max_length=2, blank=True)
    fieldrep = models.CharField(max_length=3, blank=True)
    firstname = models.CharField(max_length=20, blank=True)
    name1 = models.CharField(max_length=31, blank=True)
    nameg = models.CharField(max_length=31, blank=True)
    addressg = models.CharField(max_length=31, blank=True)
    cityg = models.CharField(max_length=20, blank=True)
    stateg = models.CharField(max_length=2, blank=True)
    zipg = models.CharField(max_length=10, blank=True)
    homephoneg = models.CharField(max_length=13, blank=True)
    workphoneg = models.CharField(max_length=13, blank=True)
    instg = models.CharField(max_length=7, blank=True)
    jobstew = models.CharField(max_length=20, blank=True)
    rcvdt = models.DateField(null=True, blank=True)
    article = models.CharField(max_length=40, blank=True)
    section = models.CharField(max_length=21, blank=True)
    explanatn = models.CharField(max_length=88, blank=True)
    level1 = models.CharField(max_length=3, blank=True)
    grant1a = models.CharField(max_length=1, blank=True)
    grant1b = models.CharField(max_length=1, blank=True)
    level2 = models.CharField(max_length=3, blank=True)
    grant2 = models.CharField(max_length=1, blank=True)
    level3 = models.CharField(max_length=3, blank=True)
    arb3 = models.CharField(max_length=3, blank=True)
    response3 = models.DateField(null=True, blank=True)
    nudged3 = models.DateField(null=True, blank=True)
    recieve3 = models.DateField(null=True, blank=True)
    advto4 = models.DateField(null=True, blank=True)
    level4 = models.CharField(max_length=3, blank=True)
    arbn4 = models.CharField(max_length=1, blank=True)
    response4 = models.DateField(null=True, blank=True)
    nudged4 = models.DateField(null=True, blank=True)
    recieve4 = models.DateField(null=True, blank=True)
    wonlost = models.CharField(max_length=3, blank=True)
    closedtg = models.DateField(null=True, blank=True)
    closedth = models.DateField(null=True, blank=True)
    fileextg = models.IntegerField(null=True, blank=True)
    arbdate = models.DateField(null=True, blank=True)
    g_num = models.IntegerField(null=True, blank=True)
    cdcref = models.CharField(max_length=20, blank=True)
    dparef = models.CharField(max_length=10, blank=True)
    pulldate = models.DateField(null=True, blank=True)
    pullwho = models.CharField(max_length=28, blank=True)
    n01 = models.CharField(max_length=80, blank=True)
    headq = models.CharField(max_length=1, blank=True)
    n02 = models.CharField(max_length=80, blank=True)
    gdeadfile = models.DateField(null=True, blank=True)
    clerk = models.CharField(max_length=10, blank=True)
    status = models.CharField(max_length=3, blank=True)
    dateassn = models.DateField(null=True, blank=True)
    staffassn = models.CharField(max_length=3, blank=True)
    onetwo = models.DateField(null=True, blank=True)
    twothree = models.DateField(null=True, blank=True)
    onereturn = models.DateField(null=True, blank=True)
    twoappeal = models.DateField(null=True, blank=True)
    twodue = models.DateField(null=True, blank=True)
    tworeturn = models.DateField(null=True, blank=True)
    threereturn = models.DateField(null=True, blank=True)
    fourtoarb = models.DateField(null=True, blank=True)
    threeappeal = models.DateField(null=True, blank=True)
    threedue = models.DateField(null=True, blank=True)
    fourdue = models.DateField(null=True, blank=True)
    fourappeal = models.DateField(null=True, blank=True)
    othermou = models.CharField(max_length=7, blank=True)
    othermou2 = models.CharField(max_length=38, blank=True)
    regiong = models.CharField(max_length=1, blank=True)
    occode = models.CharField(max_length=3, blank=True)
    arbcode = models.CharField(max_length=3, blank=True)
    response1 = models.DateField(null=True, blank=True)
    recieve1 = models.DateField(null=True, blank=True)
    miniarb = models.CharField(max_length=3, blank=True)
    response2 = models.DateField(null=True, blank=True)
    recieve2 = models.DateField(null=True, blank=True)
    altrdpa = models.DateField(null=True, blank=True)
    frrecdue = models.DateField(null=True, blank=True)
    frreccom = models.DateField(null=True, blank=True)
    dteclerk = models.DateField(null=True, blank=True)
    fcdtelgl = models.DateField(null=True, blank=True)
    abeycde = models.CharField(max_length=3, blank=True)
    oppcode = models.CharField(max_length=3, blank=True)
    staffclose = models.DateField(null=True, blank=True)
    deadappdte = models.DateField(null=True, blank=True)
    deadappsup = models.CharField(max_length=3, blank=True)
    dataentry = models.DateField(null=True, blank=True)
    fileclerk = models.DateField(null=True, blank=True)
    chappres = models.CharField(max_length=30, blank=True)
    abeyheld = models.DateField(null=True, blank=True)
    abeylevel = models.CharField(max_length=1, blank=True)
    abeysup = models.CharField(max_length=20, blank=True)
    abeycomm = models.CharField(max_length=20, blank=True)
    abeyrm = models.DateField(null=True, blank=True)
    othermou3 = models.CharField(max_length=7, blank=True)
    othermou4 = models.CharField(max_length=38, blank=True)
    othermou5 = models.CharField(max_length=7, blank=True)
    othermou6 = models.CharField(max_length=38, blank=True)
    othermou7 = models.CharField(max_length=7, blank=True)
    othermou8 = models.CharField(max_length=38, blank=True)
    othermou9 = models.CharField(max_length=7, blank=True)
    othermou10 = models.CharField(max_length=38, blank=True)
    othermou11 = models.CharField(max_length=7, blank=True)
    othermou12 = models.CharField(max_length=38, blank=True)
    paperdte = models.DateField(null=True, blank=True)
    holiday = models.CharField(max_length=1, blank=True)
    nuds = models.DateField(null=True, blank=True)
    nudt = models.DateField(null=True, blank=True)
    nudtt = models.DateField(null=True, blank=True)
    nudttt = models.DateField(null=True, blank=True)
    cr00 = models.CharField(max_length=3, blank=True)
    swor00 = models.DateField(null=True, blank=True)
    arbreqw = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    gcrstat = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'grev'

class Grevcodes(models.Model):
    grevcode = models.CharField(max_length=3)
    grevdesc = models.CharField(max_length=80)
    class Meta:
        db_table = 'grevcodes'

class Helpsys(models.Model):
    h_id = models.IntegerField(null=True, blank=True)
    h_seq = models.CharField(max_length=4, blank=True)
    h_text = models.CharField(max_length=200, blank=True)
    class Meta:
        db_table = 'helpsys'

class Holidays(models.Model):
    date_id = models.CharField(max_length=19, blank=True)
    year_num = models.CharField(max_length=4, blank=True)
    ydt_name = models.CharField(max_length=30, blank=True)
    ytd_start_dt = models.CharField(max_length=19, blank=True)
    tyd_end_dt = models.CharField(max_length=19, blank=True)
    quarter_num = models.CharField(max_length=1, blank=True)
    month_num = models.CharField(max_length=2, blank=True)
    month_name = models.CharField(max_length=20, blank=True)
    month_str = models.CharField(max_length=2, blank=True)
    day_num = models.CharField(max_length=1, blank=True)
    period = models.CharField(max_length=1, blank=True)
    y2k_period = models.CharField(max_length=6, blank=True)
    day_of_week = models.CharField(max_length=9, blank=True)
    fiscal_year = models.CharField(max_length=8, blank=True)
    holiday = models.CharField(max_length=1, blank=True)
    real_date = models.DateField(null=True, blank=True)
    hol_sup = models.CharField(max_length=1, blank=True)
    hol_fed = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'holidays'

class Hotel(models.Model):
    cc_no = models.CharField(max_length=20, blank=True)
    exp_date = models.TextField(blank=True)
    acct = models.CharField(max_length=1, blank=True)
    hfirst_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    chapter = models.CharField(max_length=7, blank=True)
    haddress = models.CharField(max_length=30, blank=True)
    hcity = models.CharField(max_length=20, blank=True)
    hstate = models.CharField(max_length=2, blank=True)
    hzip = models.CharField(max_length=20, blank=True)
    arrive = models.DateField(null=True, blank=True)
    depart = models.DateField(null=True, blank=True)
    sgldbl = models.CharField(max_length=1, blank=True)
    mon = models.CharField(max_length=1, blank=True)
    tue = models.CharField(max_length=1, blank=True)
    wed = models.CharField(max_length=1, blank=True)
    thu = models.CharField(max_length=1, blank=True)
    fri = models.CharField(max_length=1, blank=True)
    sat = models.CharField(max_length=1, blank=True)
    sun = models.CharField(max_length=1, blank=True)
    occup = models.CharField(max_length=1, blank=True)
    beds = models.CharField(max_length=1, blank=True)
    req = models.CharField(max_length=80, blank=True)
    confirm = models.DateField(null=True, blank=True)
    alt = models.CharField(max_length=1, blank=True)
    del_field = models.CharField(max_length=1, db_column='del', blank=True) # Field renamed because it was a Python reserved word.
    adult = models.CharField(max_length=2, blank=True)
    child = models.CharField(max_length=2, blank=True)
    shc = models.CharField(max_length=3, blank=True)
    shcname = models.CharField(max_length=40, blank=True)
    sha = models.CharField(max_length=3, blank=True)
    shalname = models.CharField(max_length=25, blank=True)
    shaname = models.CharField(max_length=40, blank=True)
    vip = models.CharField(max_length=1, blank=True)
    mon2 = models.CharField(max_length=1, blank=True)
    tue2 = models.CharField(max_length=1, blank=True)
    wed2 = models.CharField(max_length=1, blank=True)
    thu2 = models.CharField(max_length=1, blank=True)
    fri2 = models.CharField(max_length=1, blank=True)
    sat2 = models.CharField(max_length=1, blank=True)
    sun2 = models.CharField(max_length=1, blank=True)
    artdte = models.CharField(max_length=25, blank=True)
    arthrs = models.SmallIntegerField(null=True, blank=True)
    hotid_no = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'hotel'

class Inst(models.Model):
    iname = models.CharField(max_length=30, blank=True)
    iattn = models.CharField(max_length=40, blank=True)
    iaddress = models.CharField(max_length=30, blank=True)
    izip = models.CharField(max_length=10, blank=True)
    iphone = models.CharField(max_length=12, blank=True)
    iabbr = models.CharField(max_length=7, blank=True)
    iagency = models.CharField(max_length=23, blank=True)
    iunit = models.CharField(max_length=23, blank=True)
    inors = models.CharField(max_length=1, blank=True)
    tot = models.IntegerField(null=True, blank=True)
    iid_no = models.IntegerField()
    izipe = models.CharField(max_length=4, blank=True)
    runtot = models.IntegerField(null=True, blank=True)
    emprel = models.CharField(max_length=30, blank=True)
    ifax = models.CharField(max_length=12, blank=True)
    ipres = models.CharField(max_length=30, blank=True)
    iero = models.CharField(max_length=40, blank=True)
    ierophone = models.CharField(max_length=13, blank=True)
    ierox = models.CharField(max_length=5, blank=True)
    ierofax = models.CharField(max_length=13, blank=True)
    ilra = models.CharField(max_length=40, blank=True)
    ilraphone = models.CharField(max_length=13, blank=True)
    ilrax = models.CharField(max_length=5, blank=True)
    class Meta:
        db_table = 'inst'

class IntApps(models.Model):
    appsid_no = models.IntegerField()
    pgrpid_no = models.IntegerField(null=True, blank=True)
    app_name = models.CharField(max_length=25, blank=True)
    class Meta:
        db_table = 'int_apps'

class IntAppsPath(models.Model):
    apps_path_id = models.IntegerField()
    app_name = models.CharField(max_length=20, blank=True)
    app_path = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'int_apps_path'

class IntAuth(models.Model):
    authid_no = models.IntegerField()
    aempid_no = models.IntegerField(null=True, blank=True)
    agrpid_no = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'int_auth'

class IntGroups(models.Model):
    grpid_no = models.IntegerField()
    grp_name = models.CharField(max_length=25, blank=True)
    class Meta:
        db_table = 'int_groups'

class It(models.Model):
    itid_no = models.IntegerField()
    name = models.CharField(max_length=20)
    company = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=20)
    csz = models.CharField(max_length=20)
    class Meta:
        db_table = 'it'

class Jtitle(models.Model):
    jtitle_id = models.IntegerField()
    jtitle_txt = models.CharField(max_length=35, blank=True)
    class Meta:
        db_table = 'jtitle'

class Lab146Data(models.Model):
    id = models.IntegerField()
    id_no = models.IntegerField()
    contactdate = models.DateField(null=True, blank=True)
    classification = models.CharField(max_length=20, blank=True)
    effectivedate = models.DateField(null=True, blank=True)
    contactinfo = models.CharField(max_length=4000, blank=True)
    transferdemolayoff = models.CharField(max_length=20, blank=True)
    tdlposition = models.CharField(max_length=50, blank=True)
    tdllocation = models.CharField(max_length=50, blank=True)
    appealbasisstatement = models.CharField(max_length=4000, blank=True)
    rightslettersent = models.DateField(null=True, blank=True)
    ldrpdate = models.DateTimeField(null=True, blank=True)
    ldrpstatus = models.CharField(max_length=50, blank=True)
    attorney = models.CharField(max_length=100, blank=True)
    dateappealfiled = models.DateField(null=True, blank=True)
    sauaction = models.CharField(max_length=500, blank=True)
    dateofpsc = models.DateField(null=True, blank=True)
    appeallettersent = models.DateField(null=True, blank=True)
    enteredby = models.CharField(max_length=100, blank=True)
    filenumber = models.CharField(max_length=25, blank=True)
    class Meta:
        db_table = 'lab146data'

class Licenses(models.Model):
    liid_no = models.IntegerField()
    li_join = models.IntegerField()
    li_date = models.DateField(null=True, blank=True)
    li_name = models.CharField(max_length=25, blank=True)
    li_numb = models.CharField(max_length=50, blank=True)
    li_note = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'licenses'

class Loba(models.Model):
    filenum = models.IntegerField(null=True, blank=True)
    fileext = models.IntegerField(null=True, blank=True)
    subext = models.CharField(max_length=2, blank=True)
    sbnum = models.CharField(max_length=4, blank=True)
    abnum = models.CharField(max_length=4, blank=True)
    prefix = models.CharField(max_length=3)
    yr = models.CharField(max_length=4)
    title = models.CharField(max_length=32, blank=True)
    servdt = models.DateField()
    subtit = models.CharField(max_length=32, blank=True)
    closeddt = models.DateField(null=True, blank=True)
    subtits = models.CharField(max_length=32, blank=True)
    author = models.CharField(max_length=32, blank=True)
    scrnum = models.CharField(max_length=4, blank=True)
    scanum = models.CharField(max_length=4, blank=True)
    hrnum = models.CharField(max_length=4, blank=True)
    class Meta:
        db_table = 'loba'

class Machines(models.Model):
    chid_no = models.IntegerField()
    manu = models.CharField(max_length=20)
    mother = models.CharField(max_length=20, blank=True)
    clock = models.CharField(max_length=4)
    ram = models.CharField(max_length=4)
    nic = models.CharField(max_length=20, blank=True)
    hdd = models.CharField(max_length=20, blank=True)
    system_ssn = models.CharField(max_length=20)
    muser = models.CharField(max_length=3)
    status = models.CharField(max_length=10, blank=True)
    mach_note = models.CharField(max_length=50, blank=True)
    os = models.CharField(max_length=15, blank=True)
    model = models.CharField(max_length=20, blank=True)
    mach_name = models.CharField(max_length=15, blank=True)
    ip = models.CharField(max_length=15, blank=True)
    login = models.CharField(max_length=20, blank=True)
    passwd = models.CharField(max_length=20, blank=True)
    nic2 = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'machines'

class Maillist2(models.Model):
    name2 = models.CharField(max_length=30, blank=True)
    first_name2 = models.CharField(max_length=20, blank=True)
    office2 = models.CharField(max_length=30, blank=True)
    address2 = models.CharField(max_length=30, blank=True)
    zip2 = models.CharField(max_length=10, blank=True)
    sdate2 = models.CharField(max_length=8, blank=True)
    sfile2 = models.CharField(max_length=15, blank=True)
    zipext2 = models.CharField(max_length=4, blank=True)
    class Meta:
        db_table = 'maillist2'

class MemScoPersNos(models.Model):
    id = models.IntegerField()
    ssn = models.CharField(max_length=9)
    pernr = models.CharField(max_length=9)
    sco_no = models.CharField(max_length=10)
    class Meta:
        db_table = 'mem_sco_pers_nos'

class Member(models.Model):
    name = models.CharField(max_length=21)
    first_name = models.CharField(max_length=21)
    address = models.CharField(max_length=35, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    ssn = models.CharField(max_length=11)
    phone = models.CharField(max_length=13, blank=True)
    birthday = models.DateField(null=True, blank=True)
    rforsup = models.CharField(max_length=1, blank=True)
    minst = models.CharField(max_length=7)
    stat = models.CharField(max_length=3, blank=True)
    effdate = models.DateField(null=True, blank=True)
    sepdate = models.DateField(null=True, blank=True)
    reason = models.IntegerField(null=True, blank=True)
    jobtitle = models.IntegerField(null=True, blank=True)
    bdmbr = models.CharField(max_length=1, blank=True)
    intermit = models.CharField(max_length=1, blank=True)
    id_no = models.IntegerField()
    filebatch = models.DateField(null=True, blank=True)
    lastupdte = models.DateField(null=True, blank=True)
    zipext = models.CharField(max_length=4, blank=True)
    survey = models.CharField(max_length=1, blank=True)
    markings = models.CharField(max_length=1, blank=True)
    shift = models.CharField(max_length=3, blank=True)
    mailer = models.CharField(max_length=1, blank=True)
    bylaw97 = models.CharField(max_length=1, blank=True)
    pmb = models.CharField(max_length=13, blank=True)
    email = models.CharField(max_length=50, blank=True)
    fsdt = models.DateField(null=True, blank=True)
    retro = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'member'

class MemberContactUpdate(models.Model):
    pri_key = models.IntegerField()
    member_id = models.IntegerField()
    address = models.CharField(max_length=150, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=150, blank=True)
    taken_by = models.CharField(max_length=50)
    date = models.DateField()
    class Meta:
        db_table = 'member_contact_update'

class MemberElist(models.Model):
    group_name = models.TextField(blank=True)
    email_addr = models.TextField(blank=True)
    class Meta:
        db_table = 'member_elist'

class Membereventcodes(models.Model):
    mevcode_join = models.CharField(max_length=3)
    mevcode_code = models.CharField(max_length=25, blank=True)
    class Meta:
        db_table = 'membereventcodes'

class Memberevents(models.Model):
    meventid_no = models.IntegerField()
    mevent_join = models.IntegerField()
    mevent_entr = models.DateField(null=True, blank=True)
    mevent_date = models.DateField(null=True, blank=True)
    mevent_code = models.CharField(max_length=3, blank=True)
    mevent_note = models.CharField(max_length=25, blank=True)
    class Meta:
        db_table = 'memberevents'

class Memberpernr(models.Model):
    ssn = models.CharField(max_length=11, blank=True)
    pernr = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = 'memberpernr'

class Membership(models.Model):
    id_no = models.IntegerField()
    mrtype = models.CharField(max_length=1, blank=True)
    msocial = models.CharField(max_length=11)
    mfname = models.CharField(max_length=1, blank=True)
    mminitial = models.CharField(max_length=1, blank=True)
    mlname = models.CharField(max_length=13, blank=True)
    magency = models.CharField(max_length=3, blank=True)
    mrunit = models.CharField(max_length=3, blank=True)
    mtotprem = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    mpptype = models.CharField(max_length=1, blank=True)
    mdmo = models.CharField(max_length=2, blank=True)
    mdyr = models.CharField(max_length=4, blank=True)
    mdedcode = models.CharField(max_length=3, blank=True)
    morgcode = models.CharField(max_length=3, blank=True)
    mdedamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    mwarrantno = models.IntegerField(null=True, blank=True)
    mformat = models.CharField(max_length=1, blank=True)
    mflex = models.CharField(max_length=1, blank=True)
    mfilecode = models.CharField(max_length=3, blank=True)
    msortru = models.CharField(max_length=3, blank=True)
    mshamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    meom = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'membership'

class Menuitem(models.Model):
    imenuname = models.CharField(max_length=10, blank=True)
    itemnum = models.IntegerField(null=True, blank=True)
    mtext = models.CharField(max_length=60, blank=True)
    mtype = models.CharField(max_length=1, blank=True)
    progname = models.CharField(max_length=60, blank=True)
    nextmenu = models.CharField(max_length=10, blank=True)
    item_id = models.IntegerField()
    class Meta:
        db_table = 'menuitem'

class Menus(models.Model):
    menuname = models.CharField(max_length=10)
    title = models.CharField(max_length=60, blank=True)
    spacing = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'menus'

class Mod(models.Model):
    fileno = models.CharField(max_length=8, blank=True)
    employee = models.CharField(max_length=30, blank=True)
    instm = models.CharField(max_length=8, blank=True)
    actions = models.IntegerField(null=True, blank=True)
    priors = models.CharField(max_length=3, blank=True)
    mpenal = models.CharField(max_length=20, blank=True)
    meffect = models.DateField(null=True, blank=True)
    mmodify = models.CharField(max_length=30, blank=True)
    eth = models.CharField(max_length=10, blank=True)
    gedr = models.CharField(max_length=1, blank=True)
    mnote = models.CharField(max_length=160, blank=True)
    class Meta:
        db_table = 'mod'

class Mou(models.Model):
    mouid_no = models.IntegerField()
    mou_sec = models.CharField(max_length=12)
    class Meta:
        db_table = 'mou'

class Mreas(models.Model):
    mreas_txt = models.CharField(max_length=35, blank=True)
    mreas_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'mreas'

class Nego(models.Model):
    gneg_no = models.IntegerField()
    neg_no = models.IntegerField(null=True, blank=True)
    negtype = models.CharField(max_length=2, blank=True)
    negnumg = models.IntegerField(null=True, blank=True)
    negext = models.IntegerField(null=True, blank=True)
    lglnegnum = models.IntegerField(null=True, blank=True)
    negdate = models.DateField(null=True, blank=True)
    negyr = models.CharField(max_length=2, blank=True)
    nfieldrep = models.CharField(max_length=3, blank=True)
    hqfile = models.CharField(max_length=1, blank=True)
    nfirstname = models.CharField(max_length=20, blank=True)
    nname1 = models.CharField(max_length=31, blank=True)
    nnameg = models.CharField(max_length=31, blank=True)
    naddressg = models.CharField(max_length=31, blank=True)
    ncityg = models.CharField(max_length=20, blank=True)
    nstateg = models.CharField(max_length=2, blank=True)
    nzipg = models.CharField(max_length=10, blank=True)
    nhomephoneg = models.CharField(max_length=13, blank=True)
    nworkphoneg = models.CharField(max_length=13, blank=True)
    ninstg = models.CharField(max_length=7, blank=True)
    njobstew = models.CharField(max_length=20, blank=True)
    nrcvdt = models.DateField(null=True, blank=True)
    narticle = models.CharField(max_length=40, blank=True)
    nsection = models.CharField(max_length=21, blank=True)
    nexplanatn = models.CharField(max_length=88, blank=True)
    nlevel1 = models.CharField(max_length=1, blank=True)
    ngrant1a = models.CharField(max_length=1, blank=True)
    ngrant1b = models.CharField(max_length=1, blank=True)
    nlevel2 = models.CharField(max_length=1, blank=True)
    ngrant2 = models.CharField(max_length=1, blank=True)
    nlevel3 = models.CharField(max_length=1, blank=True)
    narb3 = models.CharField(max_length=1, blank=True)
    nresponse3 = models.DateField(null=True, blank=True)
    nnudged3 = models.DateField(null=True, blank=True)
    nrecieve3 = models.DateField(null=True, blank=True)
    nadvto4 = models.DateField(null=True, blank=True)
    nlevel4 = models.CharField(max_length=1, blank=True)
    narbn4 = models.CharField(max_length=1, blank=True)
    nresponse4 = models.DateField(null=True, blank=True)
    nnudged4 = models.DateField(null=True, blank=True)
    nrecieve4 = models.DateField(null=True, blank=True)
    nwonlost = models.CharField(max_length=1, blank=True)
    nclosedtg = models.DateField(null=True, blank=True)
    nfileextg = models.IntegerField(null=True, blank=True)
    narbdate = models.DateField(null=True, blank=True)
    sclosedtg = models.DateField(null=True, blank=True)
    ncurstat = models.CharField(max_length=3, blank=True)
    reportx = models.CharField(max_length=100, blank=True)
    nnote = models.CharField(max_length=20, blank=True)
    fnote = models.TextField(blank=True)
    class Meta:
        db_table = 'nego'

class Note(models.Model):
    note_id = models.IntegerField(null=True, blank=True)
    note_txt = models.CharField(max_length=120, blank=True)
    class Meta:
        db_table = 'note'

class OatsEmploymentType(models.Model):
    id = models.IntegerField()
    emply_typ_name = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'oats_employment_type'

class OatsFaq(models.Model):
    id = models.IntegerField()
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)
    class Meta:
        db_table = 'oats_faq'

class OatsGm(models.Model):
    gmuser = models.TextField(blank=True)
    gmday = models.IntegerField(null=True, blank=True)
    gmjob_name = models.TextField(blank=True)
    gmminutes = models.SmallIntegerField(null=True, blank=True)
    gmcode = models.TextField(blank=True)
    gmdesc = models.TextField(blank=True)
    class Meta:
        db_table = 'oats_gm'

class OatsGtype(models.Model):
    gtypeid_no = models.IntegerField()
    gtype_desc = models.TextField(blank=True)
    gtype_code = models.CharField(max_length=3, blank=True)
    gtype_actv = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'oats_gtype'

class OatsJobs(models.Model):
    oats_jobs_id = models.IntegerField()
    user = models.TextField(blank=True)
    job_name = models.TextField(blank=True)
    account_num = models.TextField(blank=True)
    supervisor = models.TextField(blank=True)
    supervisor_email = models.TextField(blank=True)
    department = models.TextField(blank=True)
    employment_type = models.TextField(blank=True)
    fill_in_hours = models.CharField(max_length=3, blank=True)
    payrate = models.FloatField(null=True, blank=True)
    is_supervisor = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'oats_jobs'

class OatsJobsNew(models.Model):
    id = models.IntegerField()
    user = models.TextField(blank=True)
    job_name = models.TextField(blank=True)
    account_num = models.TextField(blank=True)
    supervisor = models.TextField(blank=True)
    supervisor_email = models.TextField(blank=True)
    department = models.TextField(blank=True)
    employment_type = models.TextField(blank=True)
    fill_in_hours = models.CharField(max_length=3, blank=True)
    payrate = models.FloatField(null=True, blank=True)
    is_supervisor = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'oats_jobs_new'

class OatsLeaveTimeReductions(models.Model):
    transid_no = models.IntegerField(null=True, blank=True)
    id = models.IntegerField()
    empid_no = models.IntegerField()
    date_reduced = models.DateField(null=True, blank=True)
    payperiod_reduced = models.CharField(max_length=21, blank=True)
    hours_reduced = models.DecimalField(null=True, max_digits=16, decimal_places=2, blank=True)
    date_accrued = models.DateField(null=True, blank=True)
    hours_accrued = models.DecimalField(null=True, max_digits=16, decimal_places=2, blank=True)
    time_type = models.CharField(max_length=2, blank=True)
    buy_out_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'oats_leave_time_reductions'

class OatsManagers(models.Model):
    id = models.IntegerField()
    full_name = models.CharField(max_length=50, blank=True)
    class_code = models.CharField(max_length=11, blank=True)
    class Meta:
        db_table = 'oats_managers'

class OatsNc(models.Model):
    ncuser = models.TextField(blank=True)
    ncday = models.IntegerField(null=True, blank=True)
    ncjob_name = models.TextField(blank=True)
    ncminutes = models.SmallIntegerField(null=True, blank=True)
    nccode = models.TextField(blank=True)
    class Meta:
        db_table = 'oats_nc'

class OatsPersonalInfo(models.Model):
    user = models.TextField()
    fullname = models.TextField(blank=True)
    email = models.TextField(blank=True)
    id_num = models.TextField(blank=True)
    mailbox_num = models.TextField(blank=True)
    default_job = models.TextField(blank=True)
    initials = models.TextField(blank=True)
    class Meta:
        db_table = 'oats_personal_info'

class OatsSickleaveTime(models.Model):
    id = models.IntegerField()
    active = models.IntegerField(null=True, blank=True)
    empid_no = models.IntegerField(null=True, blank=True)
    sickleave_time = models.FloatField(null=True, blank=True)
    last_pay_prd_update = models.TextField(blank=True)
    last_accrued_date = models.TextField(blank=True)
    last_reduced_date = models.TextField(blank=True)
    class Meta:
        db_table = 'oats_sickleave_time'

class OatsTime(models.Model):
    id = models.IntegerField()
    user = models.TextField(blank=True)
    day = models.IntegerField(null=True, blank=True)
    job_name = models.TextField(blank=True)
    minutes = models.SmallIntegerField(null=True, blank=True)
    sequence = models.SmallIntegerField(null=True, blank=True)
    code = models.TextField(blank=True)
    cat = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'oats_time'

class OatsTimeTmp(models.Model):
    id = models.IntegerField()
    user = models.TextField(blank=True)
    day = models.IntegerField(null=True, blank=True)
    job_name = models.TextField(blank=True)
    minutes = models.SmallIntegerField(null=True, blank=True)
    sequence = models.SmallIntegerField(null=True, blank=True)
    code = models.TextField(blank=True)
    cat = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'oats_time_tmp'

class OatsTtype(models.Model):
    ttypeid_no = models.IntegerField()
    ttype_desc = models.TextField(blank=True)
    ttype_code = models.CharField(max_length=3, blank=True)
    ttype_actv = models.SmallIntegerField(null=True, blank=True)
    ttype_cat = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'oats_ttype'

class OatsUsers(models.Model):
    id = models.IntegerField()
    user = models.TextField(blank=True)
    password = models.TextField(blank=True)
    lastlogin = models.DateTimeField(null=True, blank=True)
    numlogins = models.IntegerField(null=True, blank=True)
    current = models.IntegerField(null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'oats_users'

class OatsVacationTime(models.Model):
    id = models.IntegerField()
    active = models.IntegerField(null=True, blank=True)
    empid_no = models.IntegerField(null=True, blank=True)
    vacation_time = models.FloatField(null=True, blank=True)
    last_pay_prd_update = models.TextField(blank=True)
    last_accrued_date = models.TextField(blank=True)
    last_reduced_date = models.TextField(blank=True)
    class Meta:
        db_table = 'oats_vacation_time'

class Office(models.Model):
    off_id = models.IntegerField(null=True, blank=True)
    off_bdmbr = models.CharField(max_length=1, blank=True)
    off_chaprs = models.CharField(max_length=1, blank=True)
    off_exec = models.CharField(max_length=1, blank=True)
    off_phone = models.CharField(max_length=13, blank=True)
    off_cphone = models.CharField(max_length=13, blank=True)
    off_ext = models.CharField(max_length=4, blank=True)
    off_start = models.DateField(null=True, blank=True)
    off_end = models.DateField(null=True, blank=True)
    off_js = models.CharField(max_length=1, blank=True)
    off_cjs = models.CharField(max_length=1, blank=True)
    off_phlog = models.CharField(max_length=1, blank=True)
    off_don = models.CharField(max_length=1, blank=True)
    off_pos1 = models.CharField(max_length=8, blank=True)
    off_pos2 = models.CharField(max_length=8, blank=True)
    off_pos3 = models.CharField(max_length=8, blank=True)
    off_pos4 = models.CharField(max_length=8, blank=True)
    off_yr1 = models.CharField(max_length=6, blank=True)
    off_yr2 = models.CharField(max_length=6, blank=True)
    off_yr3 = models.CharField(max_length=6, blank=True)
    off_yr4 = models.CharField(max_length=6, blank=True)
    r_order = models.IntegerField(null=True, blank=True)
    committee = models.CharField(max_length=1, blank=True)
    dailylst = models.CharField(max_length=1, blank=True)
    position = models.CharField(max_length=20, blank=True)
    mphone = models.CharField(max_length=13, blank=True)
    class Meta:
        db_table = 'office'

class Oppose(models.Model):
    opname = models.CharField(max_length=30, blank=True)
    opfirstname = models.CharField(max_length=20, blank=True)
    opaddress = models.CharField(max_length=50, blank=True)
    opcity = models.CharField(max_length=20, blank=True)
    opstate = models.CharField(max_length=2, blank=True)
    opzip = models.CharField(max_length=10, blank=True)
    opphone = models.CharField(max_length=13, blank=True)
    opjoincde = models.CharField(max_length=3, blank=True)
    opfax = models.CharField(max_length=13, blank=True)
    opemail = models.CharField(max_length=50, blank=True)
    opfees = models.CharField(max_length=20, blank=True)
    optitle = models.CharField(max_length=20, blank=True)
    oagency = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'oppose'

class Outlaw(models.Model):
    oname = models.CharField(max_length=30, blank=True)
    ofirstname = models.CharField(max_length=20, blank=True)
    oaddress = models.CharField(max_length=30, blank=True)
    ocity = models.CharField(max_length=20, blank=True)
    ostate = models.CharField(max_length=2, blank=True)
    ozip = models.CharField(max_length=10, blank=True)
    ophone = models.CharField(max_length=13, blank=True)
    ojoincde = models.CharField(max_length=3, blank=True)
    ofax = models.CharField(max_length=13, blank=True)
    oemail = models.CharField(max_length=50, blank=True)
    ofees = models.CharField(max_length=20, blank=True)
    otitle = models.CharField(max_length=20, blank=True)
    ocell = models.CharField(max_length=13, blank=True)
    class Meta:
        db_table = 'outlaw'

class Pa(models.Model):
    perb = models.CharField(max_length=13, blank=True)
    spb = models.CharField(max_length=6, blank=True)
    rec_no = models.IntegerField()
    casenum = models.IntegerField(null=True, blank=True)
    filenum = models.IntegerField(null=True, blank=True)
    fileext = models.CharField(max_length=2, blank=True)
    filetype = models.CharField(max_length=4, blank=True)
    yr = models.CharField(max_length=2, blank=True)
    lawyerinit = models.CharField(max_length=3, blank=True)
    pid_no = models.IntegerField(null=True, blank=True)
    pname = models.CharField(max_length=30, blank=True)
    pnameext = models.CharField(max_length=35, blank=True)
    pnameext2 = models.CharField(max_length=35, blank=True)
    paddress = models.CharField(max_length=30, blank=True)
    pcity = models.CharField(max_length=20, blank=True)
    pstate = models.CharField(max_length=2, blank=True)
    pzip = models.CharField(max_length=10, blank=True)
    pworkphone = models.CharField(max_length=13, blank=True)
    pinst = models.CharField(max_length=7, blank=True)
    action = models.CharField(max_length=50, blank=True)
    act = models.IntegerField(null=True, blank=True)
    act2 = models.IntegerField(null=True, blank=True)
    act3 = models.IntegerField(null=True, blank=True)
    preason = models.CharField(max_length=50, blank=True)
    reas = models.IntegerField(null=True, blank=True)
    reas2 = models.IntegerField(null=True, blank=True)
    reas3 = models.IntegerField(null=True, blank=True)
    assigned = models.CharField(max_length=30, blank=True)
    appealeddt = models.DateField(null=True, blank=True)
    hearingdt = models.DateField(null=True, blank=True)
    alj = models.CharField(max_length=30, blank=True)
    decisiondt = models.DateField(null=True, blank=True)
    result = models.CharField(max_length=100, blank=True)
    writofman = models.CharField(max_length=1, blank=True)
    writresult = models.CharField(max_length=40, blank=True)
    pobor = models.CharField(max_length=1, blank=True)
    harassment = models.CharField(max_length=1, blank=True)
    closeddt = models.DateField(null=True, blank=True)
    servdt = models.DateField(null=True, blank=True)
    acteffdt = models.DateField(null=True, blank=True)
    pnote = models.CharField(max_length=120, blank=True)
    region = models.CharField(max_length=1, blank=True)
    grev_num = models.FloatField(null=True, blank=True)
    p_num = models.IntegerField(null=True, blank=True)
    deadfile = models.DateField(null=True, blank=True)
    deadinsat = models.DateField(null=True, blank=True)
    pclerk = models.CharField(max_length=10, blank=True)
    pstaff2 = models.CharField(max_length=3, blank=True)
    pstaff3 = models.CharField(max_length=3, blank=True)
    pstaff4 = models.CharField(max_length=3, blank=True)
    pstaff5 = models.CharField(max_length=3, blank=True)
    pstaff6 = models.CharField(max_length=3, blank=True)
    passgn = models.DateField(null=True, blank=True)
    passgn2 = models.DateField(null=True, blank=True)
    passgn3 = models.DateField(null=True, blank=True)
    passgn4 = models.DateField(null=True, blank=True)
    poutname = models.CharField(max_length=3, blank=True)
    popname = models.CharField(max_length=3, blank=True)
    pstaffcomnt = models.CharField(max_length=30, blank=True)
    fileopen = models.DateField(null=True, blank=True)
    openby = models.CharField(max_length=20, blank=True)
    updatef1 = models.DateField(null=True, blank=True)
    f1by = models.CharField(max_length=20, blank=True)
    pdatef2 = models.DateField(null=True, blank=True)
    f2by = models.CharField(max_length=20, blank=True)
    updatef3 = models.DateField(null=True, blank=True)
    f3by = models.CharField(max_length=20, blank=True)
    updatef4 = models.DateField(null=True, blank=True)
    f4by = models.CharField(max_length=20, blank=True)
    fid_no = models.IntegerField(null=True, blank=True)
    tosuper = models.DateField(null=True, blank=True)
    tofilerm = models.DateField(null=True, blank=True)
    fcreated = models.DateField(null=True, blank=True)
    appsldcdue = models.DateField(null=True, blank=True)
    appsldcvote = models.CharField(max_length=3, blank=True)
    appecac = models.CharField(max_length=1, blank=True)
    appecacvote = models.CharField(max_length=3, blank=True)
    apppleaddue = models.DateField(null=True, blank=True)
    appfiled = models.DateField(null=True, blank=True)
    apprespdue = models.DateField(null=True, blank=True)
    appellate1 = models.CharField(max_length=3, blank=True)
    appellate2 = models.CharField(max_length=3, blank=True)
    appellate3 = models.CharField(max_length=3, blank=True)
    appdecision = models.DateField(null=True, blank=True)
    appdeccode = models.CharField(max_length=3, blank=True)
    appcomments = models.CharField(max_length=60, blank=True)
    appmotion = models.DateField(null=True, blank=True)
    psadue = models.DateField(null=True, blank=True)
    psareply = models.DateField(null=True, blank=True)
    psaresponse = models.DateField(null=True, blank=True)
    psaoraldte = models.DateField(null=True, blank=True)
    disclosure = models.DateField(null=True, blank=True)
    statutedte = models.DateField(null=True, blank=True)
    statcinf = models.DateField(null=True, blank=True)
    trialdte = models.DateField(null=True, blank=True)
    prtrialconf = models.DateField(null=True, blank=True)
    other = models.CharField(max_length=20, blank=True)
    oforum = models.CharField(max_length=20, blank=True)
    otryer = models.CharField(max_length=20, blank=True)
    otherevent = models.DateField(null=True, blank=True)
    otherresdte = models.DateField(null=True, blank=True)
    otherrescde = models.CharField(max_length=3, blank=True)
    othercom = models.CharField(max_length=60, blank=True)
    adforum = models.CharField(max_length=20, blank=True)
    adtryer = models.CharField(max_length=20, blank=True)
    addevent = models.DateField(null=True, blank=True)
    addresdte = models.DateField(null=True, blank=True)
    addrescde = models.CharField(max_length=3, blank=True)
    addcom = models.CharField(max_length=60, blank=True)
    sldcdue = models.DateField(null=True, blank=True)
    sldcvote = models.CharField(max_length=3, blank=True)
    sldcsentdte = models.DateField(null=True, blank=True)
    sldcvteresp = models.DateField(null=True, blank=True)
    writsldc = models.CharField(max_length=3, blank=True)
    writecac = models.CharField(max_length=3, blank=True)
    writecacvote = models.CharField(max_length=3, blank=True)
    writecacsent = models.DateField(null=True, blank=True)
    writecacresp = models.DateField(null=True, blank=True)
    writdue = models.DateField(null=True, blank=True)
    writdone = models.DateField(null=True, blank=True)
    writdfiled = models.DateField(null=True, blank=True)
    superior_no = models.IntegerField(null=True, blank=True)
    writrespdue = models.DateField(null=True, blank=True)
    supjudge = models.CharField(max_length=20, blank=True)
    writdecision = models.DateField(null=True, blank=True)
    writresultcde = models.CharField(max_length=3, blank=True)
    writcasenotes = models.CharField(max_length=60, blank=True)
    writheardte = models.DateField(null=True, blank=True)
    servicedte = models.DateField(null=True, blank=True)
    spbappldte = models.DateField(null=True, blank=True)
    ldcappr = models.CharField(max_length=3, blank=True)
    sldcsubdte = models.DateField(null=True, blank=True)
    sldcappr = models.CharField(max_length=3, blank=True)
    ldcresp1 = models.DateField(null=True, blank=True)
    ldcresp2 = models.DateField(null=True, blank=True)
    ldcresp3 = models.DateField(null=True, blank=True)
    ldcresp4 = models.DateField(null=True, blank=True)
    ecacsubdte = models.DateField(null=True, blank=True)
    ecacappr = models.CharField(max_length=3, blank=True)
    ecacresp1 = models.DateField(null=True, blank=True)
    ecacresp2 = models.DateField(null=True, blank=True)
    ecacresp3 = models.DateField(null=True, blank=True)
    ecacresp4 = models.DateField(null=True, blank=True)
    petrehear = models.CharField(max_length=1, blank=True)
    skellydte = models.DateField(null=True, blank=True)
    skellyresult = models.CharField(max_length=3, blank=True)
    disccldte = models.DateField(null=True, blank=True)
    spbrescde = models.CharField(max_length=3, blank=True)
    spbcom = models.CharField(max_length=60, blank=True)
    sldcdte2 = models.DateField(null=True, blank=True)
    sldcresp1 = models.DateField(null=True, blank=True)
    sldcresp2 = models.DateField(null=True, blank=True)
    sldcresp3 = models.DateField(null=True, blank=True)
    sldcresp4 = models.DateField(null=True, blank=True)
    ecacsubdte2 = models.DateField(null=True, blank=True)
    ecac2resp1 = models.DateField(null=True, blank=True)
    ecac2resp2 = models.DateField(null=True, blank=True)
    ecac2resp3 = models.DateField(null=True, blank=True)
    ecac2resp4 = models.DateField(null=True, blank=True)
    rehearduedte = models.DateField(null=True, blank=True)
    rerespdue = models.DateField(null=True, blank=True)
    reheardec = models.DateField(null=True, blank=True)
    petrescde = models.CharField(max_length=3, blank=True)
    petrehcom = models.CharField(max_length=60, blank=True)
    dfby = models.CharField(max_length=15, blank=True)
    currentstat = models.CharField(max_length=3, blank=True)
    currentcomment = models.CharField(max_length=60, blank=True)
    currentdt = models.DateField(null=True, blank=True)
    subxx = models.CharField(max_length=1, blank=True)
    reduction = models.CharField(max_length=2, blank=True)
    month = models.CharField(max_length=2, blank=True)
    suspendfor = models.CharField(max_length=3, blank=True)
    demotrank = models.CharField(max_length=4, blank=True)
    dupq = models.CharField(max_length=1, blank=True)
    apdte = models.DateField(null=True, blank=True)
    apcde = models.CharField(max_length=3, blank=True)
    ldcdte = models.DateField(null=True, blank=True)
    ldrpcde = models.CharField(max_length=3, blank=True)
    deccde = models.CharField(max_length=3, blank=True)
    ecacdte = models.DateField(null=True, blank=True)
    ecaccde = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'pa'

class Paact(models.Model):
    paact_id = models.IntegerField()
    paact_stext = models.CharField(max_length=30, blank=True)
    paact_ltext = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'paact'

class Par(models.Model):
    par_id = models.IntegerField()
    par_stext = models.CharField(max_length=30, blank=True)
    par_ltext = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'par'

class Payarb(models.Model):
    payid_no = models.IntegerField()
    pay_join = models.IntegerField()
    paystat = models.CharField(max_length=1, blank=True)
    paydate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'payarb'

class Payarbcode(models.Model):
    pdsocial = models.CharField(max_length=11)
    pdcodee = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'payarbcode'

class Payarbcollect(models.Model):
    pmsocial = models.CharField(max_length=11)
    pmfname = models.CharField(max_length=1, blank=True)
    pmlname = models.CharField(max_length=13, blank=True)
    pmdmo = models.CharField(max_length=2, blank=True)
    pmdyr = models.CharField(max_length=4, blank=True)
    pmdedamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    pm0705 = models.CharField(max_length=1, blank=True)
    pm0805 = models.CharField(max_length=1, blank=True)
    pm0905 = models.CharField(max_length=1, blank=True)
    pm1005 = models.CharField(max_length=1, blank=True)
    pm1105 = models.CharField(max_length=1, blank=True)
    pm1205 = models.CharField(max_length=1, blank=True)
    pm0106 = models.CharField(max_length=1, blank=True)
    pm0206 = models.CharField(max_length=1, blank=True)
    pm0306 = models.CharField(max_length=1, blank=True)
    pm0406 = models.CharField(max_length=1, blank=True)
    pm0506 = models.CharField(max_length=1, blank=True)
    pm0606 = models.CharField(max_length=1, blank=True)
    pm0706 = models.CharField(max_length=1, blank=True)
    pm0806 = models.CharField(max_length=1, blank=True)
    pm0906 = models.CharField(max_length=1, blank=True)
    pm1006 = models.CharField(max_length=1, blank=True)
    pm1106 = models.CharField(max_length=1, blank=True)
    pm1206 = models.CharField(max_length=1, blank=True)
    pstotmo = models.CharField(max_length=2, blank=True)
    pmcode = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'payarbcollect'

class Payarbmemhist(models.Model):
    pmsocial = models.CharField(max_length=11)
    pmfname = models.CharField(max_length=1, blank=True)
    pmlname = models.CharField(max_length=13, blank=True)
    pmdmo = models.CharField(max_length=2, blank=True)
    pmdyr = models.CharField(max_length=4, blank=True)
    pmdedamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    pm0705 = models.CharField(max_length=1, blank=True)
    pm0805 = models.CharField(max_length=1, blank=True)
    pm0905 = models.CharField(max_length=1, blank=True)
    pm1005 = models.CharField(max_length=1, blank=True)
    pm1105 = models.CharField(max_length=1, blank=True)
    pm1205 = models.CharField(max_length=1, blank=True)
    pm0106 = models.CharField(max_length=1, blank=True)
    pm0206 = models.CharField(max_length=1, blank=True)
    pm0306 = models.CharField(max_length=1, blank=True)
    pm0406 = models.CharField(max_length=1, blank=True)
    pm0506 = models.CharField(max_length=1, blank=True)
    pm0606 = models.CharField(max_length=1, blank=True)
    pm0706 = models.CharField(max_length=1, blank=True)
    pm0806 = models.CharField(max_length=1, blank=True)
    pm0906 = models.CharField(max_length=1, blank=True)
    pm1006 = models.CharField(max_length=1, blank=True)
    pm1106 = models.CharField(max_length=1, blank=True)
    pm1206 = models.CharField(max_length=1, blank=True)
    pstotmo = models.CharField(max_length=2, blank=True)
    pmcode = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'payarbmemhist'

class Payarbscohist(models.Model):
    psfacility = models.TextField(blank=True)
    pssocial = models.CharField(max_length=11)
    psinitial = models.CharField(max_length=2, blank=True)
    pslname = models.CharField(max_length=25, blank=True)
    psn = models.CharField(max_length=16, blank=True)
    ps0705 = models.CharField(max_length=1, blank=True)
    ps0805 = models.CharField(max_length=1, blank=True)
    ps0905 = models.CharField(max_length=1, blank=True)
    ps1005 = models.CharField(max_length=1, blank=True)
    ps1105 = models.CharField(max_length=1, blank=True)
    ps1205 = models.CharField(max_length=1, blank=True)
    ps0106 = models.CharField(max_length=1, blank=True)
    ps0206 = models.CharField(max_length=1, blank=True)
    ps0306 = models.CharField(max_length=1, blank=True)
    ps0406 = models.CharField(max_length=1, blank=True)
    ps0506 = models.CharField(max_length=1, blank=True)
    ps0606 = models.CharField(max_length=1, blank=True)
    ps0706 = models.CharField(max_length=1, blank=True)
    ps0806 = models.CharField(max_length=1, blank=True)
    ps0906 = models.CharField(max_length=1, blank=True)
    ps1006 = models.CharField(max_length=1, blank=True)
    ps1106 = models.CharField(max_length=1, blank=True)
    ps1206 = models.CharField(max_length=1, blank=True)
    pstotmo = models.CharField(max_length=2, blank=True)
    pscomment = models.TextField(blank=True)
    class Meta:
        db_table = 'payarbscohist'

class Payarbscomail(models.Model):
    pssocial = models.CharField(max_length=4)
    psinitial = models.CharField(max_length=1, blank=True)
    pslname = models.CharField(max_length=25, blank=True)
    psdmo = models.CharField(max_length=2, blank=True)
    psdyr = models.CharField(max_length=4, blank=True)
    psdedamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    ps0705 = models.CharField(max_length=1, blank=True)
    ps0805 = models.CharField(max_length=1, blank=True)
    ps0905 = models.CharField(max_length=1, blank=True)
    ps1005 = models.CharField(max_length=1, blank=True)
    ps1105 = models.CharField(max_length=1, blank=True)
    ps1205 = models.CharField(max_length=1, blank=True)
    ps0106 = models.CharField(max_length=1, blank=True)
    ps0206 = models.CharField(max_length=1, blank=True)
    ps0306 = models.CharField(max_length=1, blank=True)
    ps0406 = models.CharField(max_length=1, blank=True)
    ps0506 = models.CharField(max_length=1, blank=True)
    ps0606 = models.CharField(max_length=1, blank=True)
    ps0706 = models.CharField(max_length=1, blank=True)
    ps0806 = models.CharField(max_length=1, blank=True)
    ps0906 = models.CharField(max_length=1, blank=True)
    ps1006 = models.CharField(max_length=1, blank=True)
    ps1106 = models.CharField(max_length=1, blank=True)
    ps1206 = models.CharField(max_length=1, blank=True)
    pstotmo = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = 'payarbscomail'

class Pba(models.Model):
    pba_ssn = models.CharField(max_length=11)
    class Meta:
        db_table = 'pba'

class Pbr(models.Model):
    pbr_ssn = models.CharField(max_length=11, blank=True)
    class Meta:
        db_table = 'pbr'

class Peacek(models.Model):
    pkid_no = models.IntegerField()
    volume = models.CharField(max_length=3)
    issue = models.CharField(max_length=2)
    issue_dt = models.CharField(max_length=20)
    cover = models.CharField(max_length=40, blank=True)
    dept = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30, blank=True)
    desc = models.CharField(max_length=200, blank=True)
    page_no = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'peacek'

class Piduction(models.Model):
    prtype = models.CharField(max_length=1, blank=True)
    psocial = models.CharField(max_length=11)
    pfname = models.CharField(max_length=1, blank=True)
    pminitial = models.CharField(max_length=1, blank=True)
    plname = models.CharField(max_length=13, blank=True)
    pagency = models.CharField(max_length=3, blank=True)
    prunit = models.CharField(max_length=3, blank=True)
    ptotprem = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    ppptype = models.CharField(max_length=1, blank=True)
    pdmo = models.CharField(max_length=2, blank=True)
    pdyr = models.CharField(max_length=4, blank=True)
    pdedcode = models.CharField(max_length=3, blank=True)
    porgcode = models.CharField(max_length=3, blank=True)
    pdedamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    pwarrantno = models.IntegerField(null=True, blank=True)
    pformat = models.CharField(max_length=1, blank=True)
    pflex = models.CharField(max_length=1, blank=True)
    pfilecode = models.CharField(max_length=3, blank=True)
    psortru = models.CharField(max_length=3, blank=True)
    pshamount = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    class Meta:
        db_table = 'piduction'

class Quest(models.Model):
    qssn = models.CharField(max_length=11)
    quest1 = models.CharField(max_length=8, blank=True)
    quest2 = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'quest'

class Receive(models.Model):
    reid_no = models.IntegerField()
    rerep = models.CharField(max_length=3)
    carrier = models.CharField(max_length=3)
    redate = models.DateField()
    sender = models.CharField(max_length=20)
    cartons = models.SmallIntegerField()
    ship_id = models.CharField(max_length=20)
    renotes = models.CharField(max_length=50, blank=True)
    adresse = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'receive'

class RetroTracking(models.Model):
    retro_no = models.IntegerField()
    ssn = models.TextField()
    retro_count = models.BigIntegerField()
    date_updated = models.DateField()
    class Meta:
        db_table = 'retro_tracking'

class Rights(models.Model):
    vname = models.CharField(max_length=30, blank=True)
    vfirstname = models.CharField(max_length=20, blank=True)
    vgroup = models.CharField(max_length=40, blank=True)
    vaddress = models.CharField(max_length=30, blank=True)
    vzip = models.CharField(max_length=10, blank=True)
    vphone = models.CharField(max_length=12, blank=True)
    vtitle = models.CharField(max_length=20, blank=True)
    vagency = models.CharField(max_length=23, blank=True)
    vregion = models.CharField(max_length=1, blank=True)
    vid_no = models.IntegerField()
    vlast = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'rights'

class Ring(models.Model):
    ringer = models.IntegerField()
    sizel = models.CharField(max_length=20, blank=True)
    sizes = models.CharField(max_length=20, blank=True)
    bezel = models.CharField(max_length=20, blank=True)
    payroll = models.CharField(max_length=20, blank=True)
    daterc = models.DateField(null=True, blank=True)
    dater1 = models.DateField(null=True, blank=True)
    dater2 = models.DateField(null=True, blank=True)
    dater3 = models.DateField(null=True, blank=True)
    visa = models.CharField(max_length=20, blank=True)
    mc = models.CharField(max_length=20, blank=True)
    visaexp = models.DateField(null=True, blank=True)
    mcexp = models.DateField(null=True, blank=True)
    checkx = models.DateField(null=True, blank=True)
    mcvisachk = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=80, blank=True)
    howmany = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'ring'

class Rtb(models.Model):
    rtbid_no = models.IntegerField()
    rtbmem_no = models.IntegerField()
    rtbfname = models.CharField(max_length=21, blank=True)
    rtblname = models.CharField(max_length=21, blank=True)
    rtbinst = models.CharField(max_length=9, blank=True)
    rbank = models.CharField(max_length=3)
    redate = models.DateField()
    rreceipt_no = models.IntegerField(null=True, blank=True)
    rtbcredit = models.SmallIntegerField(null=True, blank=True)
    rreason = models.CharField(max_length=3, blank=True)
    rudate = models.CharField(max_length=200, blank=True)
    runote = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'rtb'

class Rtbbcodes(models.Model):
    rtbbcode = models.CharField(max_length=3)
    rtbbdesc = models.CharField(max_length=25, blank=True)
    class Meta:
        db_table = 'rtbbcodes'

class Rtbrcodes(models.Model):
    rtbrcode = models.CharField(max_length=3)
    rtbrdesc = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'rtbrcodes'

class Runits(models.Model):
    unitcode = models.CharField(max_length=3)
    unitdesc = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'runits'

class Sched(models.Model):
    casenumber = models.CharField(max_length=10, blank=True)
    shearing = models.DateField(null=True, blank=True)
    sname = models.CharField(max_length=40, blank=True)
    appealof = models.CharField(max_length=40, blank=True)
    place = models.CharField(max_length=40, blank=True)
    htime = models.CharField(max_length=5, blank=True)
    represent = models.CharField(max_length=25, blank=True)
    snotes = models.CharField(max_length=40, blank=True)
    stime = models.IntegerField(null=True, blank=True)
    htimeh = models.IntegerField(null=True, blank=True)
    htimem = models.IntegerField(null=True, blank=True)
    spb = models.CharField(max_length=6, blank=True)
    class Meta:
        db_table = 'sched'

class Sex(models.Model):
    sex_no = models.IntegerField(null=True, blank=True)
    leave1 = models.DateField(null=True, blank=True)
    leave2 = models.DateField(null=True, blank=True)
    ozip = models.CharField(max_length=10, blank=True)
    namewas = models.CharField(max_length=21, blank=True)
    fsdate1 = models.DateField(null=True, blank=True)
    fsdate2 = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    beni = models.CharField(max_length=120, blank=True)
    ozipext = models.CharField(max_length=4, blank=True)
    class Meta:
        db_table = 'sex'

class Shawn1(models.Model):
    stmem1 = models.CharField(max_length=3, blank=True)
    stmem = models.CharField(max_length=20, blank=True)
    stmem2 = models.CharField(max_length=3, blank=True)
    stmem3 = models.CharField(max_length=3, blank=True)
    stmem4 = models.CharField(max_length=3, blank=True)
    stmem5 = models.CharField(max_length=3, blank=True)
    stmem6 = models.CharField(max_length=3, blank=True)
    office = models.CharField(max_length=1, blank=True)
    semail = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'shawn1'

class Shippers(models.Model):
    shipnam = models.CharField(max_length=3)
    shipdesc = models.CharField(max_length=40)
    class Meta:
        db_table = 'shippers'

class Stats(models.Model):
    statu = models.CharField(max_length=3)
    desc = models.CharField(max_length=80, blank=True)
    this = models.CharField(max_length=30, blank=True)
    ded_amt = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    class Meta:
        db_table = 'stats'

class Steward(models.Model):
    sid_no = models.IntegerField(null=True, blank=True)
    p1 = models.CharField(max_length=1, blank=True)
    p2 = models.CharField(max_length=1, blank=True)
    p3 = models.CharField(max_length=1, blank=True)
    p1date = models.DateField(null=True, blank=True)
    p2date = models.DateField(null=True, blank=True)
    p3date = models.DateField(null=True, blank=True)
    certify = models.DateField(null=True, blank=True)
    resigned = models.CharField(max_length=1, blank=True)
    rdate = models.DateField(null=True, blank=True)
    dismiss = models.CharField(max_length=1, blank=True)
    ddate = models.DateField(null=True, blank=True)
    phase4 = models.CharField(max_length=1, blank=True)
    phase4dt = models.DateField(null=True, blank=True)
    ma = models.CharField(max_length=1, blank=True)
    madt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'steward'

class Sucaba(models.Model):
    date0 = models.DateField(null=True, blank=True)
    date1 = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'sucaba'

class Sysaggregates(models.Model):
    name = models.TextField(blank=True)
    owner = models.CharField(max_length=32, blank=True)
    aggid = models.IntegerField(null=True, blank=True)
    init_func = models.TextField(blank=True)
    iter_func = models.TextField(blank=True)
    combine_func = models.TextField(blank=True)
    final_func = models.TextField(blank=True)
    handlesnulls = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = 'sysaggregates'

class Sysams(models.Model):
    am_name = models.TextField(blank=True)
    am_owner = models.CharField(max_length=32, blank=True)
    am_id = models.IntegerField(null=True, blank=True)
    am_type = models.CharField(max_length=1, blank=True)
    am_sptype = models.CharField(max_length=3, blank=True)
    am_defopclass = models.IntegerField(null=True, blank=True)
    am_keyscan = models.IntegerField(null=True, blank=True)
    am_unique = models.IntegerField(null=True, blank=True)
    am_cluster = models.IntegerField(null=True, blank=True)
    am_rowids = models.IntegerField(null=True, blank=True)
    am_readwrite = models.IntegerField(null=True, blank=True)
    am_parallel = models.IntegerField(null=True, blank=True)
    am_costfactor = models.FloatField(null=True, blank=True)
    am_create = models.IntegerField(null=True, blank=True)
    am_drop = models.IntegerField(null=True, blank=True)
    am_open = models.IntegerField(null=True, blank=True)
    am_close = models.IntegerField(null=True, blank=True)
    am_insert = models.IntegerField(null=True, blank=True)
    am_delete = models.IntegerField(null=True, blank=True)
    am_update = models.IntegerField(null=True, blank=True)
    am_stats = models.IntegerField(null=True, blank=True)
    am_scancost = models.IntegerField(null=True, blank=True)
    am_check = models.IntegerField(null=True, blank=True)
    am_beginscan = models.IntegerField(null=True, blank=True)
    am_endscan = models.IntegerField(null=True, blank=True)
    am_rescan = models.IntegerField(null=True, blank=True)
    am_getnext = models.IntegerField(null=True, blank=True)
    am_getbyid = models.IntegerField(null=True, blank=True)
    am_build = models.IntegerField(null=True, blank=True)
    am_init = models.IntegerField(null=True, blank=True)
    am_truncate = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysams'

class Sysattrtypes(models.Model):
    extended_id = models.IntegerField(null=True, blank=True)
    seqno = models.SmallIntegerField(null=True, blank=True)
    levelno = models.SmallIntegerField(null=True, blank=True)
    parent_no = models.SmallIntegerField(null=True, blank=True)
    fieldname = models.TextField(blank=True)
    fieldno = models.SmallIntegerField(null=True, blank=True)
    type = models.SmallIntegerField(null=True, blank=True)
    length = models.SmallIntegerField(null=True, blank=True)
    xtd_type_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysattrtypes'

class Sysautolocate(models.Model):
    dbsnum = models.IntegerField(null=True, blank=True)
    dbsname = models.TextField(blank=True)
    pagesize = models.SmallIntegerField(null=True, blank=True)
    flags = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysautolocate'

class Sysblobs(models.Model):
    spacename = models.TextField(blank=True)
    type = models.CharField(max_length=1, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    colno = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysblobs'

class Syscasts(models.Model):
    owner = models.CharField(max_length=32, blank=True)
    argument_type = models.SmallIntegerField(null=True, blank=True)
    argument_xid = models.IntegerField(null=True, blank=True)
    result_type = models.SmallIntegerField(null=True, blank=True)
    result_xid = models.IntegerField(null=True, blank=True)
    routine_name = models.TextField(blank=True)
    routine_owner = models.CharField(max_length=32, blank=True)
    class_field = models.CharField(max_length=1, db_column='class', blank=True) # Field renamed because it was a Python reserved word.
    class Meta:
        db_table = 'syscasts'

class Syschecks(models.Model):
    constrid = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=1, blank=True)
    seqno = models.SmallIntegerField(null=True, blank=True)
    checktext = models.CharField(max_length=32, blank=True)
    class Meta:
        db_table = 'syschecks'

class Syscolattribs(models.Model):
    tabid = models.IntegerField(null=True, blank=True)
    colno = models.SmallIntegerField(null=True, blank=True)
    extentsize = models.IntegerField(null=True, blank=True)
    flags = models.IntegerField(null=True, blank=True)
    flags1 = models.IntegerField(null=True, blank=True)
    sbspace = models.TextField(blank=True)
    class Meta:
        db_table = 'syscolattribs'

class Syscolauth(models.Model):
    grantor = models.CharField(max_length=32, blank=True)
    grantee = models.CharField(max_length=32, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    colno = models.SmallIntegerField(null=True, blank=True)
    colauth = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'syscolauth'

class Syscoldepend(models.Model):
    constrid = models.IntegerField(null=True, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    colno = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'syscoldepend'

class Syscolinput(models.Model):
    owner = models.CharField(max_length=32, blank=True)
    tabname = models.CharField(max_length=32, blank=True)
    colname = models.CharField(max_length=32, blank=True)
    extowner = models.CharField(max_length=32, blank=True)
    attrname = models.CharField(max_length=10, blank=True)
    attrval = models.CharField(max_length=128, blank=True)
    class Meta:
        db_table = 'syscolinput'

class Syscolumnext(models.Model):
    owner = models.CharField(max_length=32, blank=True)
    tabname = models.CharField(max_length=32, blank=True)
    colname = models.CharField(max_length=32, blank=True)
    extowner = models.CharField(max_length=32, blank=True)
    colalias = models.CharField(max_length=32, blank=True)
    collabel = models.CharField(max_length=32, blank=True)
    coltitle = models.CharField(max_length=32, blank=True)
    remarks = models.CharField(max_length=254, blank=True)
    subtype = models.CharField(max_length=4, blank=True)
    class_field = models.CharField(max_length=32, db_column='class', blank=True) # Field renamed because it was a Python reserved word.
    class Meta:
        db_table = 'syscolumnext'

class Syscolumns(models.Model):
    colname = models.TextField(blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    colno = models.SmallIntegerField(null=True, blank=True)
    coltype = models.SmallIntegerField(null=True, blank=True)
    collength = models.SmallIntegerField(null=True, blank=True)
    colmin = models.IntegerField(null=True, blank=True)
    colmax = models.IntegerField(null=True, blank=True)
    extended_id = models.IntegerField(null=True, blank=True)
    seclabelid = models.IntegerField(null=True, blank=True)
    colattr = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'syscolumns'

class Sysconstraints(models.Model):
    constrid = models.IntegerField(null=True, blank=True)
    constrname = models.TextField(blank=True)
    owner = models.CharField(max_length=32, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    constrtype = models.CharField(max_length=1, blank=True)
    idxname = models.TextField(blank=True)
    collation = models.CharField(max_length=36, blank=True)
    class Meta:
        db_table = 'sysconstraints'

class Sysdefaults(models.Model):
    tabid = models.IntegerField(null=True, blank=True)
    colno = models.SmallIntegerField(null=True, blank=True)
    type = models.CharField(max_length=1, blank=True)
    default = models.CharField(max_length=256, blank=True)
    class_field = models.CharField(max_length=1, db_column='class', blank=True) # Field renamed because it was a Python reserved word.
    class Meta:
        db_table = 'sysdefaults'

class Sysdepend(models.Model):
    btabid = models.IntegerField(null=True, blank=True)
    btype = models.CharField(max_length=1, blank=True)
    dtabid = models.IntegerField(null=True, blank=True)
    dtype = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'sysdepend'

class Sysdirectives(models.Model):
    id = models.IntegerField(null=True, blank=True)
    query = models.TextField(blank=True) # This field type is a guess.
    directive = models.TextField(blank=True) # This field type is a guess.
    directivecode = models.TextField(blank=True) # This field type is a guess.
    active = models.SmallIntegerField(null=True, blank=True)
    hashcode = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysdirectives'

class Sysdistrib(models.Model):
    tabid = models.IntegerField(null=True, blank=True)
    colno = models.SmallIntegerField(null=True, blank=True)
    seqno = models.IntegerField(null=True, blank=True)
    constructed = models.DateField(null=True, blank=True)
    mode = models.CharField(max_length=1, blank=True)
    resolution = models.FloatField(null=True, blank=True)
    confidence = models.FloatField(null=True, blank=True)
    encdat = models.TextField(blank=True) # This field type is a guess.
    type = models.CharField(max_length=1, blank=True)
    smplsize = models.FloatField(null=True, blank=True)
    rowssmpld = models.FloatField(null=True, blank=True)
    constr_time = models.DateTimeField(null=True, blank=True)
    ustnrows = models.FloatField(null=True, blank=True)
    ustbuildduration = models.TextField(blank=True) # This field type is a guess.
    nupdates = models.FloatField(null=True, blank=True)
    ndeletes = models.FloatField(null=True, blank=True)
    ninserts = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'sysdistrib'

class Sysdomains(models.Model):
    id = models.IntegerField()
    owner = models.CharField(max_length=32, blank=True)
    name = models.TextField(blank=True)
    type = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysdomains'

class Syserrors(models.Model):
    sqlstate = models.CharField(max_length=5, blank=True)
    locale = models.CharField(max_length=36, blank=True)
    level = models.SmallIntegerField(null=True, blank=True)
    seqno = models.SmallIntegerField(null=True, blank=True)
    message = models.TextField(blank=True)
    class Meta:
        db_table = 'syserrors'

class Sysextcols(models.Model):
    tabid = models.IntegerField(null=True, blank=True)
    colno = models.SmallIntegerField(null=True, blank=True)
    exttype = models.SmallIntegerField(null=True, blank=True)
    extstart = models.SmallIntegerField(null=True, blank=True)
    extlength = models.SmallIntegerField(null=True, blank=True)
    nullstr = models.CharField(max_length=256, blank=True)
    decprec = models.SmallIntegerField(null=True, blank=True)
    extstype = models.TextField(blank=True)
    class Meta:
        db_table = 'sysextcols'

class Sysextdfiles(models.Model):
    tabid = models.IntegerField(null=True, blank=True)
    dfentry = models.CharField(max_length=469, blank=True)
    blobdir = models.CharField(max_length=344, blank=True)
    clobdir = models.CharField(max_length=344, blank=True)
    class Meta:
        db_table = 'sysextdfiles'

class Sysexternal(models.Model):
    tabid = models.IntegerField(null=True, blank=True)
    fmttype = models.CharField(max_length=1, blank=True)
    codeset = models.TextField(blank=True)
    recdelim = models.TextField(blank=True)
    flddelim = models.CharField(max_length=4, blank=True)
    datefmt = models.CharField(max_length=8, blank=True)
    moneyfmt = models.CharField(max_length=20, blank=True)
    maxerrors = models.IntegerField(null=True, blank=True)
    rejectfile = models.CharField(max_length=464, blank=True)
    flags = models.IntegerField(null=True, blank=True)
    ndfiles = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysexternal'

class Sysfragauth(models.Model):
    grantor = models.CharField(max_length=32, blank=True)
    grantee = models.CharField(max_length=32, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    fragment = models.TextField(blank=True)
    fragauth = models.CharField(max_length=6, blank=True)
    class Meta:
        db_table = 'sysfragauth'

class Sysfragdist(models.Model):
    tabid = models.IntegerField(null=True, blank=True)
    fragid = models.IntegerField(null=True, blank=True)
    colno = models.SmallIntegerField(null=True, blank=True)
    seqno = models.SmallIntegerField(null=True, blank=True)
    mode = models.CharField(max_length=1, blank=True)
    resolution = models.FloatField(null=True, blank=True)
    confidence = models.FloatField(null=True, blank=True)
    rowssmpld = models.FloatField(null=True, blank=True)
    constr_time = models.DateTimeField(null=True, blank=True)
    ustbuildduration = models.TextField(blank=True) # This field type is a guess.
    ustnrows = models.FloatField(null=True, blank=True)
    minibinsize = models.FloatField(null=True, blank=True)
    nupdates = models.FloatField(null=True, blank=True)
    ndeletes = models.FloatField(null=True, blank=True)
    ninserts = models.FloatField(null=True, blank=True)
    version = models.IntegerField(null=True, blank=True)
    dbsnum = models.IntegerField(null=True, blank=True)
    encdist = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'sysfragdist'

class Sysfragments(models.Model):
    fragtype = models.CharField(max_length=1, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    indexname = models.TextField(blank=True)
    colno = models.IntegerField(null=True, blank=True)
    partn = models.IntegerField(null=True, blank=True)
    strategy = models.CharField(max_length=1, blank=True)
    location = models.CharField(max_length=1, blank=True)
    servername = models.TextField(blank=True)
    evalpos = models.IntegerField(null=True, blank=True)
    exprtext = models.TextField(blank=True) # This field type is a guess.
    exprbin = models.TextField(blank=True) # This field type is a guess.
    exprarr = models.TextField(blank=True) # This field type is a guess.
    flags = models.IntegerField(null=True, blank=True)
    dbspace = models.TextField(blank=True)
    levels = models.SmallIntegerField(null=True, blank=True)
    npused = models.FloatField(null=True, blank=True)
    nrows = models.FloatField(null=True, blank=True)
    clust = models.FloatField(null=True, blank=True)
    partition = models.TextField(blank=True)
    version = models.SmallIntegerField(null=True, blank=True)
    nupdates = models.FloatField(null=True, blank=True)
    ndeletes = models.FloatField(null=True, blank=True)
    ninserts = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'sysfragments'

class Sysindexes(models.Model):
    idxname = models.TextField(blank=True)
    owner = models.CharField(max_length=32, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    idxtype = models.CharField(max_length=1, blank=True)
    clustered = models.CharField(max_length=1, blank=True)
    part1 = models.SmallIntegerField(null=True, blank=True)
    part2 = models.SmallIntegerField(null=True, blank=True)
    part3 = models.SmallIntegerField(null=True, blank=True)
    part4 = models.SmallIntegerField(null=True, blank=True)
    part5 = models.SmallIntegerField(null=True, blank=True)
    part6 = models.SmallIntegerField(null=True, blank=True)
    part7 = models.SmallIntegerField(null=True, blank=True)
    part8 = models.SmallIntegerField(null=True, blank=True)
    part9 = models.SmallIntegerField(null=True, blank=True)
    part10 = models.SmallIntegerField(null=True, blank=True)
    part11 = models.SmallIntegerField(null=True, blank=True)
    part12 = models.SmallIntegerField(null=True, blank=True)
    part13 = models.SmallIntegerField(null=True, blank=True)
    part14 = models.SmallIntegerField(null=True, blank=True)
    part15 = models.SmallIntegerField(null=True, blank=True)
    part16 = models.SmallIntegerField(null=True, blank=True)
    levels = models.SmallIntegerField(null=True, blank=True)
    leaves = models.FloatField(null=True, blank=True)
    nunique = models.FloatField(null=True, blank=True)
    clust = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'sysindexes'

class Sysindices(models.Model):
    idxname = models.TextField(blank=True)
    owner = models.CharField(max_length=32, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    idxtype = models.CharField(max_length=1, blank=True)
    clustered = models.CharField(max_length=1, blank=True)
    levels = models.SmallIntegerField(null=True, blank=True)
    leaves = models.FloatField(null=True, blank=True)
    nunique = models.FloatField(null=True, blank=True)
    clust = models.FloatField(null=True, blank=True)
    nrows = models.FloatField(null=True, blank=True)
    indexkeys = models.TextField(blank=True) # This field type is a guess.
    amid = models.IntegerField(null=True, blank=True)
    amparam = models.TextField(blank=True)
    collation = models.CharField(max_length=36, blank=True)
    pagesize = models.IntegerField(null=True, blank=True)
    nhashcols = models.SmallIntegerField(null=True, blank=True)
    nbuckets = models.IntegerField(null=True, blank=True)
    ustlowts = models.DateTimeField(null=True, blank=True)
    ustbuildduration = models.TextField(blank=True) # This field type is a guess.
    nupdates = models.FloatField(null=True, blank=True)
    ndeletes = models.FloatField(null=True, blank=True)
    ninserts = models.FloatField(null=True, blank=True)
    fextsize = models.IntegerField(null=True, blank=True)
    nextsize = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysindices'

class Sysinherits(models.Model):
    child = models.IntegerField(null=True, blank=True)
    parent = models.IntegerField(null=True, blank=True)
    class_field = models.CharField(max_length=1, db_column='class', blank=True) # Field renamed because it was a Python reserved word.
    class Meta:
        db_table = 'sysinherits'

class Syslangauth(models.Model):
    grantor = models.CharField(max_length=32, blank=True)
    grantee = models.CharField(max_length=32, blank=True)
    langid = models.IntegerField(null=True, blank=True)
    langauth = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'syslangauth'

class Syslogmap(models.Model):
    tabloc = models.IntegerField(null=True, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    fragid = models.IntegerField(null=True, blank=True)
    flags = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'syslogmap'

class Sysmenuitems(models.Model):
    imenuname = models.CharField(max_length=18, blank=True)
    itemnum = models.IntegerField(null=True, blank=True)
    mtext = models.CharField(max_length=60, blank=True)
    mtype = models.CharField(max_length=1, blank=True)
    progname = models.CharField(max_length=60, blank=True)
    nextmenu = models.CharField(max_length=10, blank=True)
    mcomp = models.CharField(max_length=20, blank=True)
    item_id = models.IntegerField()
    class Meta:
        db_table = 'sysmenuitems'

class Sysmenus(models.Model):
    menuname = models.CharField(max_length=18, blank=True)
    title = models.CharField(max_length=60, blank=True)
    spacing = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysmenus'

class Sysobjstate(models.Model):
    objtype = models.CharField(max_length=1, blank=True)
    owner = models.CharField(max_length=32, blank=True)
    name = models.TextField(blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'sysobjstate'

class Sysopclasses(models.Model):
    opclassname = models.TextField(blank=True)
    owner = models.CharField(max_length=32, blank=True)
    amid = models.IntegerField(null=True, blank=True)
    opclassid = models.IntegerField(null=True, blank=True)
    ops = models.TextField(blank=True)
    support = models.TextField(blank=True)
    class Meta:
        db_table = 'sysopclasses'

class Sysopclstr(models.Model):
    owner = models.CharField(max_length=32, blank=True)
    clstrname = models.TextField(blank=True)
    clstrsize = models.IntegerField(null=True, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    blobcol1 = models.SmallIntegerField(null=True, blank=True)
    blobcol2 = models.SmallIntegerField(null=True, blank=True)
    blobcol3 = models.SmallIntegerField(null=True, blank=True)
    blobcol4 = models.SmallIntegerField(null=True, blank=True)
    blobcol5 = models.SmallIntegerField(null=True, blank=True)
    blobcol6 = models.SmallIntegerField(null=True, blank=True)
    blobcol7 = models.SmallIntegerField(null=True, blank=True)
    blobcol8 = models.SmallIntegerField(null=True, blank=True)
    blobcol9 = models.SmallIntegerField(null=True, blank=True)
    blobcol10 = models.SmallIntegerField(null=True, blank=True)
    blobcol11 = models.SmallIntegerField(null=True, blank=True)
    blobcol12 = models.SmallIntegerField(null=True, blank=True)
    blobcol13 = models.SmallIntegerField(null=True, blank=True)
    blobcol14 = models.SmallIntegerField(null=True, blank=True)
    blobcol15 = models.SmallIntegerField(null=True, blank=True)
    blobcol16 = models.SmallIntegerField(null=True, blank=True)
    clstrkey1 = models.SmallIntegerField(null=True, blank=True)
    clstrkey2 = models.SmallIntegerField(null=True, blank=True)
    clstrkey3 = models.SmallIntegerField(null=True, blank=True)
    clstrkey4 = models.SmallIntegerField(null=True, blank=True)
    clstrkey5 = models.SmallIntegerField(null=True, blank=True)
    clstrkey6 = models.SmallIntegerField(null=True, blank=True)
    clstrkey7 = models.SmallIntegerField(null=True, blank=True)
    clstrkey8 = models.SmallIntegerField(null=True, blank=True)
    clstrkey9 = models.SmallIntegerField(null=True, blank=True)
    clstrkey10 = models.SmallIntegerField(null=True, blank=True)
    clstrkey11 = models.SmallIntegerField(null=True, blank=True)
    clstrkey12 = models.SmallIntegerField(null=True, blank=True)
    clstrkey13 = models.SmallIntegerField(null=True, blank=True)
    clstrkey14 = models.SmallIntegerField(null=True, blank=True)
    clstrkey15 = models.SmallIntegerField(null=True, blank=True)
    clstrkey16 = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysopclstr'

class Sysprocauth(models.Model):
    grantor = models.CharField(max_length=32, blank=True)
    grantee = models.CharField(max_length=32, blank=True)
    procid = models.IntegerField(null=True, blank=True)
    procauth = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'sysprocauth'

class Sysprocbody(models.Model):
    procid = models.IntegerField(null=True, blank=True)
    datakey = models.CharField(max_length=1, blank=True)
    seqno = models.IntegerField(null=True, blank=True)
    data = models.CharField(max_length=256, blank=True)
    class Meta:
        db_table = 'sysprocbody'

class Sysproccolumns(models.Model):
    procid = models.IntegerField(null=True, blank=True)
    paramid = models.IntegerField(null=True, blank=True)
    paramname = models.TextField(blank=True)
    paramtype = models.SmallIntegerField(null=True, blank=True)
    paramlen = models.SmallIntegerField(null=True, blank=True)
    paramxid = models.IntegerField(null=True, blank=True)
    paramattr = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysproccolumns'

class Sysprocedures(models.Model):
    procname = models.TextField(blank=True)
    owner = models.CharField(max_length=32, blank=True)
    procid = models.IntegerField(null=True, blank=True)
    mode = models.CharField(max_length=1, blank=True)
    retsize = models.IntegerField(null=True, blank=True)
    symsize = models.IntegerField(null=True, blank=True)
    datasize = models.IntegerField(null=True, blank=True)
    codesize = models.IntegerField(null=True, blank=True)
    numargs = models.IntegerField(null=True, blank=True)
    isproc = models.CharField(max_length=1, blank=True)
    specificname = models.TextField(blank=True)
    externalname = models.TextField(blank=True)
    paramstyle = models.CharField(max_length=1, blank=True)
    langid = models.IntegerField(null=True, blank=True)
    paramtypes = models.TextField(blank=True) # This field type is a guess.
    variant = models.BooleanField(null=True, blank=True)
    client = models.BooleanField(null=True, blank=True)
    handlesnulls = models.BooleanField(null=True, blank=True)
    iterator = models.BooleanField(null=True, blank=True)
    percallcost = models.IntegerField(null=True, blank=True)
    commutator = models.TextField(blank=True)
    negator = models.TextField(blank=True)
    selfunc = models.TextField(blank=True)
    internal = models.BooleanField(null=True, blank=True)
    class_field = models.CharField(max_length=18, db_column='class', blank=True) # Field renamed because it was a Python reserved word.
    stack = models.IntegerField(null=True, blank=True)
    parallelizable = models.BooleanField(null=True, blank=True)
    costfunc = models.TextField(blank=True)
    selconst = models.FloatField(null=True, blank=True)
    collation = models.CharField(max_length=36, blank=True)
    procflags = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysprocedures'

class Sysprocplan(models.Model):
    procid = models.IntegerField(null=True, blank=True)
    planid = models.IntegerField(null=True, blank=True)
    datakey = models.CharField(max_length=1, blank=True)
    seqno = models.IntegerField(null=True, blank=True)
    created = models.DateField(null=True, blank=True)
    datasize = models.IntegerField(null=True, blank=True)
    data = models.CharField(max_length=256, blank=True)
    class Meta:
        db_table = 'sysprocplan'

class Sysreferences(models.Model):
    constrid = models.IntegerField(null=True, blank=True)
    primary = models.IntegerField(null=True, blank=True)
    ptabid = models.IntegerField(null=True, blank=True)
    updrule = models.CharField(max_length=1, blank=True)
    delrule = models.CharField(max_length=1, blank=True)
    matchtype = models.CharField(max_length=1, blank=True)
    pendant = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'sysreferences'

class Sysroleauth(models.Model):
    rolename = models.CharField(max_length=32, blank=True)
    grantee = models.CharField(max_length=32, blank=True)
    is_grantable = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'sysroleauth'

class Sysroutinelangs(models.Model):
    langid = models.IntegerField(null=True, blank=True)
    langname = models.CharField(max_length=30, blank=True)
    langinitfunc = models.TextField(blank=True)
    langpath = models.CharField(max_length=255, blank=True)
    langclass = models.CharField(max_length=18, blank=True)
    class Meta:
        db_table = 'sysroutinelangs'

class Sysseclabelauth(models.Model):
    grantee = models.CharField(max_length=32, blank=True)
    secpolicyid = models.IntegerField(null=True, blank=True)
    readseclabelid = models.IntegerField(null=True, blank=True)
    writeseclabelid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysseclabelauth'

class Sysseclabelcomponentelements(models.Model):
    compid = models.IntegerField(null=True, blank=True)
    element = models.TextField(blank=True)
    elementencoding = models.CharField(max_length=8, blank=True)
    parentelement = models.TextField(blank=True)
    alterversion = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysseclabelcomponentelements'

class Sysseclabelcomponents(models.Model):
    compname = models.TextField(blank=True)
    compid = models.IntegerField(null=True, blank=True)
    comptype = models.CharField(max_length=1, blank=True)
    numelements = models.IntegerField(null=True, blank=True)
    coveringinfo = models.TextField(blank=True)
    numalters = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysseclabelcomponents'

class Sysseclabelnames(models.Model):
    secpolicyid = models.IntegerField(null=True, blank=True)
    seclabelname = models.TextField(blank=True)
    seclabelid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysseclabelnames'

class Sysseclabels(models.Model):
    secpolicyid = models.IntegerField(null=True, blank=True)
    seclabelid = models.IntegerField(null=True, blank=True)
    seclabelencoding = models.TextField(blank=True)
    class Meta:
        db_table = 'sysseclabels'

class Syssecpolicies(models.Model):
    secpolicyname = models.TextField(blank=True)
    secpolicyid = models.IntegerField(null=True, blank=True)
    numcomps = models.SmallIntegerField(null=True, blank=True)
    comptypelist = models.CharField(max_length=16, blank=True)
    overrideseclabel = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'syssecpolicies'

class Syssecpolicycomponents(models.Model):
    secpolicyid = models.IntegerField(null=True, blank=True)
    compid = models.IntegerField(null=True, blank=True)
    compno = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'syssecpolicycomponents'

class Syssecpolicyexemptions(models.Model):
    grantee = models.CharField(max_length=32, blank=True)
    secpolicyid = models.IntegerField(null=True, blank=True)
    exemption = models.CharField(max_length=6, blank=True)
    class Meta:
        db_table = 'syssecpolicyexemptions'

class Syssequences(models.Model):
    seqid = models.IntegerField(null=True, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    start_val = models.BigIntegerField(null=True, blank=True)
    inc_val = models.BigIntegerField(null=True, blank=True)
    min_val = models.BigIntegerField(null=True, blank=True)
    max_val = models.BigIntegerField(null=True, blank=True)
    cycle = models.CharField(max_length=1, blank=True)
    restart_val = models.BigIntegerField(null=True, blank=True)
    cache = models.IntegerField(null=True, blank=True)
    order = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'syssequences'

class Syssuperviews(models.Model):
    svwid = models.IntegerField(null=True, blank=True)
    owner = models.CharField(max_length=32, blank=True)
    svwname = models.CharField(max_length=32, blank=True)
    remarks = models.CharField(max_length=72, blank=True)
    class Meta:
        db_table = 'syssuperviews'

class Syssurrogateauth(models.Model):
    trusteduser = models.CharField(max_length=32, blank=True)
    surrogateuser = models.CharField(max_length=32, blank=True)
    class Meta:
        db_table = 'syssurrogateauth'

class Syssvwaliases(models.Model):
    svwid = models.IntegerField(null=True, blank=True)
    tabalias = models.CharField(max_length=32, blank=True)
    colseq = models.IntegerField(null=True, blank=True)
    colname = models.CharField(max_length=32, blank=True)
    colalias = models.CharField(max_length=32, blank=True)
    label = models.CharField(max_length=32, blank=True)
    title = models.CharField(max_length=32, blank=True)
    flag = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'syssvwaliases'

class Syssvwauth(models.Model):
    svwid = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=32, blank=True)
    svwauth = models.CharField(max_length=8, blank=True)
    rowlimit = models.IntegerField(null=True, blank=True)
    readlimit = models.IntegerField(null=True, blank=True)
    readsperrowlimit = models.FloatField(null=True, blank=True)
    elapsedtimelimit = models.IntegerField(null=True, blank=True)
    isolationmode = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'syssvwauth'

class Syssvwformats(models.Model):
    svwid = models.IntegerField(null=True, blank=True)
    colalias = models.CharField(max_length=32, blank=True)
    priority = models.SmallIntegerField(null=True, blank=True)
    typeface = models.CharField(max_length=64, blank=True)
    fontsize = models.SmallIntegerField(null=True, blank=True)
    fontstyle = models.SmallIntegerField(null=True, blank=True)
    fontcolor = models.IntegerField(null=True, blank=True)
    aidfa = models.CharField(max_length=30, blank=True)
    formatmask = models.CharField(max_length=254, blank=True)
    format4gl = models.CharField(max_length=128, blank=True)
    align = models.CharField(max_length=1, blank=True)
    case = models.CharField(max_length=1, blank=True)
    ruletype = models.CharField(max_length=1, blank=True)
    checktext = models.CharField(max_length=254, blank=True)
    class Meta:
        db_table = 'syssvwformats'

class Syssvwinput(models.Model):
    svwid = models.IntegerField(null=True, blank=True)
    colalias = models.CharField(max_length=32, blank=True)
    attrname = models.CharField(max_length=10, blank=True)
    attrval = models.CharField(max_length=128, blank=True)
    class Meta:
        db_table = 'syssvwinput'

class Syssvwjoins(models.Model):
    svwid = models.IntegerField(null=True, blank=True)
    tabalias = models.CharField(max_length=32, blank=True)
    jcolseq = models.SmallIntegerField(null=True, blank=True)
    mastercol = models.CharField(max_length=32, blank=True)
    detailcol1 = models.CharField(max_length=32, blank=True)
    detailcol2 = models.CharField(max_length=32, blank=True)
    joinoperator = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = 'syssvwjoins'

class Syssvworder(models.Model):
    svwid = models.IntegerField(null=True, blank=True)
    seqno = models.SmallIntegerField(null=True, blank=True)
    colalias = models.CharField(max_length=32, blank=True)
    sorttype = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'syssvworder'

class Syssvwtables(models.Model):
    svwid = models.IntegerField(null=True, blank=True)
    tableseq = models.IntegerField(null=True, blank=True)
    owner = models.CharField(max_length=32, blank=True)
    tabname = models.CharField(max_length=32, blank=True)
    masteralias = models.CharField(max_length=32, blank=True)
    cardinality = models.CharField(max_length=1, blank=True)
    usetype = models.CharField(max_length=1, blank=True)
    tabalias = models.CharField(max_length=32, blank=True)
    levelname = models.CharField(max_length=32, blank=True)
    remarks = models.CharField(max_length=72, blank=True)
    class Meta:
        db_table = 'syssvwtables'

class Syssynonyms(models.Model):
    owner = models.CharField(max_length=32, blank=True)
    synname = models.TextField(blank=True)
    created = models.DateField(null=True, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'syssynonyms'

class Syssyntable(models.Model):
    tabid = models.IntegerField(null=True, blank=True)
    servername = models.TextField(blank=True)
    dbname = models.TextField(blank=True)
    owner = models.CharField(max_length=32, blank=True)
    tabname = models.TextField(blank=True)
    btabid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'syssyntable'

class Systabamdata(models.Model):
    tabid = models.IntegerField(null=True, blank=True)
    am_param = models.CharField(max_length=256, blank=True)
    am_space = models.TextField(blank=True)
    class Meta:
        db_table = 'systabamdata'

class Systabauth(models.Model):
    grantor = models.CharField(max_length=32, blank=True)
    grantee = models.CharField(max_length=32, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    tabauth = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = 'systabauth'

class Systableext(models.Model):
    owner = models.CharField(max_length=32, blank=True)
    tabname = models.CharField(max_length=32, blank=True)
    extowner = models.CharField(max_length=32, blank=True)
    tabalias = models.CharField(max_length=32, blank=True)
    remarks = models.CharField(max_length=254, blank=True)
    class Meta:
        db_table = 'systableext'

class Systables(models.Model):
    tabname = models.TextField(blank=True)
    owner = models.CharField(max_length=32, blank=True)
    partnum = models.IntegerField(null=True, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    rowsize = models.SmallIntegerField(null=True, blank=True)
    ncols = models.SmallIntegerField(null=True, blank=True)
    nindexes = models.SmallIntegerField(null=True, blank=True)
    nrows = models.FloatField(null=True, blank=True)
    created = models.DateField(null=True, blank=True)
    version = models.IntegerField(null=True, blank=True)
    tabtype = models.CharField(max_length=1, blank=True)
    locklevel = models.CharField(max_length=1, blank=True)
    npused = models.FloatField(null=True, blank=True)
    fextsize = models.IntegerField(null=True, blank=True)
    nextsize = models.IntegerField(null=True, blank=True)
    flags = models.SmallIntegerField(null=True, blank=True)
    site = models.TextField(blank=True)
    dbname = models.TextField(blank=True)
    type_xid = models.IntegerField(null=True, blank=True)
    am_id = models.IntegerField(null=True, blank=True)
    pagesize = models.IntegerField(null=True, blank=True)
    ustlowts = models.DateTimeField(null=True, blank=True)
    secpolicyid = models.IntegerField(null=True, blank=True)
    protgranularity = models.CharField(max_length=1, blank=True)
    statchange = models.SmallIntegerField(null=True, blank=True)
    statlevel = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'systables'

class Systraceclasses(models.Model):
    name = models.CharField(max_length=18, blank=True)
    classid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'systraceclasses'

class Systracemsgs(models.Model):
    name = models.TextField(blank=True)
    msgid = models.IntegerField(null=True, blank=True)
    locale = models.CharField(max_length=36, blank=True)
    seqno = models.SmallIntegerField(null=True, blank=True)
    message = models.TextField(blank=True)
    class Meta:
        db_table = 'systracemsgs'

class Systrigbody(models.Model):
    trigid = models.IntegerField(null=True, blank=True)
    datakey = models.CharField(max_length=1, blank=True)
    seqno = models.IntegerField(null=True, blank=True)
    data = models.CharField(max_length=256, blank=True)
    class Meta:
        db_table = 'systrigbody'

class Systriggers(models.Model):
    trigid = models.IntegerField(null=True, blank=True)
    trigname = models.TextField(blank=True)
    owner = models.CharField(max_length=32, blank=True)
    tabid = models.IntegerField(null=True, blank=True)
    event = models.CharField(max_length=1, blank=True)
    old = models.TextField(blank=True)
    new = models.TextField(blank=True)
    mode = models.CharField(max_length=1, blank=True)
    collation = models.CharField(max_length=36, blank=True)
    class Meta:
        db_table = 'systriggers'

class Sysulist(models.Model):
    username = models.CharField(max_length=32, blank=True)
    svagrantor = models.CharField(max_length=32, blank=True)
    remarks = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = 'sysulist'

class Sysusers(models.Model):
    username = models.CharField(max_length=32, blank=True)
    usertype = models.CharField(max_length=1, blank=True)
    priority = models.SmallIntegerField(null=True, blank=True)
    password = models.CharField(max_length=16, blank=True)
    defrole = models.CharField(max_length=32, blank=True)
    class Meta:
        db_table = 'sysusers'

class Sysviews(models.Model):
    tabid = models.IntegerField(null=True, blank=True)
    seqno = models.SmallIntegerField(null=True, blank=True)
    viewtext = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = 'sysviews'

class Sysviolations(models.Model):
    targettid = models.IntegerField(null=True, blank=True)
    viotid = models.IntegerField(null=True, blank=True)
    diatid = models.IntegerField(null=True, blank=True)
    maxrows = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysviolations'

class Sysxadatasources(models.Model):
    xa_datasrc_owner = models.CharField(max_length=32, blank=True)
    xa_datasrc_name = models.TextField(blank=True)
    xa_datasrc_rmid = models.IntegerField(null=True, blank=True)
    xa_source_typeid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysxadatasources'

class Sysxasourcetypes(models.Model):
    xa_source_typeid = models.IntegerField(null=True, blank=True)
    xa_source_owner = models.CharField(max_length=32, blank=True)
    xa_source_name = models.TextField(blank=True)
    xa_flags = models.IntegerField(null=True, blank=True)
    xa_version = models.IntegerField(null=True, blank=True)
    xa_open = models.IntegerField(null=True, blank=True)
    xa_close = models.IntegerField(null=True, blank=True)
    xa_start = models.IntegerField(null=True, blank=True)
    xa_end = models.IntegerField(null=True, blank=True)
    xa_rollback = models.IntegerField(null=True, blank=True)
    xa_prepare = models.IntegerField(null=True, blank=True)
    xa_commit = models.IntegerField(null=True, blank=True)
    xa_recover = models.IntegerField(null=True, blank=True)
    xa_forget = models.IntegerField(null=True, blank=True)
    xa_complete = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysxasourcetypes'

class Sysxtddesc(models.Model):
    extended_id = models.IntegerField(null=True, blank=True)
    seqno = models.SmallIntegerField(null=True, blank=True)
    description = models.CharField(max_length=256, blank=True)
    class Meta:
        db_table = 'sysxtddesc'

class Sysxtdtypeauth(models.Model):
    grantor = models.CharField(max_length=32, blank=True)
    grantee = models.CharField(max_length=32, blank=True)
    type = models.IntegerField(null=True, blank=True)
    auth = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = 'sysxtdtypeauth'

class Sysxtdtypes(models.Model):
    extended_id = models.IntegerField(null=True, blank=True)
    domain = models.CharField(max_length=1, blank=True)
    mode = models.CharField(max_length=1, blank=True)
    owner = models.CharField(max_length=32, blank=True)
    name = models.TextField(blank=True)
    type = models.SmallIntegerField(null=True, blank=True)
    source = models.IntegerField(null=True, blank=True)
    maxlen = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    byvalue = models.CharField(max_length=1, blank=True)
    cannothash = models.CharField(max_length=1, blank=True)
    align = models.SmallIntegerField(null=True, blank=True)
    locator = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sysxtdtypes'

class TDedDet(models.Model):
    ssn = models.CharField(max_length=11, blank=True)
    f_int = models.CharField(max_length=1, blank=True)
    m_int = models.CharField(max_length=1, blank=True)
    surname = models.CharField(max_length=13, blank=True)
    agency = models.CharField(max_length=3, blank=True)
    rep_unt = models.CharField(max_length=3, blank=True)
    d_share = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    d_prem = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    period_t = models.CharField(max_length=1, blank=True)
    period_m = models.SmallIntegerField(null=True, blank=True)
    period_y = models.SmallIntegerField(null=True, blank=True)
    ded_code = models.CharField(max_length=3, blank=True)
    org_code = models.CharField(max_length=3, blank=True)
    d_ded = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    warrant = models.CharField(max_length=8, blank=True)
    format = models.CharField(max_length=1, blank=True)
    rec_type = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 't_ded_det'

class TDedTot(models.Model):
    t_share = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    t_prem = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    t_ded = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    ded_cnt = models.IntegerField(null=True, blank=True)
    ded_code = models.CharField(max_length=3, blank=True)
    org_code = models.CharField(max_length=3, blank=True)
    rec_type = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 't_ded_tot'

class TLabel(models.Model):
    volume = models.CharField(max_length=7, blank=True)
    l_date = models.DateField(null=True, blank=True)
    system = models.CharField(max_length=20, blank=True)
    l_work = models.CharField(max_length=8, blank=True)
    l_year = models.CharField(max_length=4, blank=True)
    l_day = models.IntegerField(null=True, blank=True)
    s_num = models.IntegerField()
    class Meta:
        db_table = 't_label'

class TblFiles(models.Model):
    description = models.CharField(max_length=255, blank=True)
    filename = models.CharField(max_length=255, blank=True)
    filesize = models.IntegerField(null=True, blank=True)
    filetype = models.CharField(max_length=255, blank=True)
    grpid_no = models.IntegerField(null=True, blank=True)
    id_files = models.IntegerField()
    bin_data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'tbl_files'

class Telecom(models.Model):
    telid_no = models.IntegerField()
    port_no = models.CharField(max_length=4)
    ext_no = models.SmallIntegerField()
    jack_no = models.CharField(max_length=6)
    did_no = models.CharField(max_length=13)
    user = models.CharField(max_length=3, blank=True)
    tel_no = models.CharField(max_length=13, blank=True)
    description = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'telecom'

class Testa(models.Model):
    id = models.SmallIntegerField(null=True, blank=True)
    email = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'testa'

class Testb(models.Model):
    id = models.SmallIntegerField(null=True, blank=True)
    email = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'testb'

class TicLdf(models.Model):
    case_num = models.IntegerField()
    filetp = models.CharField(max_length=2)
    tickdate = models.DateField()
    trep = models.CharField(max_length=3)
    subnum = models.CharField(max_length=2)
    subext = models.CharField(max_length=2)
    filename = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'tic_ldf'

class TicketHardware(models.Model):
    id = models.IntegerField()
    active = models.IntegerField()
    name = models.TextField()
    class Meta:
        db_table = 'ticket_hardware'

class TicketInfo(models.Model):
    id = models.IntegerField()
    user = models.TextField()
    status = models.IntegerField()
    hardware_id = models.IntegerField()
    software_id = models.IntegerField()
    emp_assigned_id = models.IntegerField()
    emp_ext = models.TextField()
    desc = models.TextField(blank=True) # This field type is a guess.
    time_submitted = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'ticket_info'

class TicketPriority(models.Model):
    id = models.IntegerField()
    priority_name = models.TextField(blank=True)
    active = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'ticket_priority'

class TicketSoftware(models.Model):
    id = models.IntegerField()
    active = models.IntegerField()
    software_name = models.TextField()
    class Meta:
        db_table = 'ticket_software'

class TicketSolution(models.Model):
    id = models.IntegerField()
    ticket_info_id = models.IntegerField()
    status = models.IntegerField()
    solution_text = models.TextField() # This field type is a guess.
    minutes = models.IntegerField()
    class Meta:
        db_table = 'ticket_solution'

class TicketStatus(models.Model):
    id = models.IntegerField()
    status_name = models.TextField()
    class Meta:
        db_table = 'ticket_status'

class Tickles(models.Model):
    case_num = models.IntegerField()
    filetp = models.CharField(max_length=2)
    tickdate = models.DateField()
    trep = models.CharField(max_length=3)
    subnum = models.CharField(max_length=2)
    subext = models.CharField(max_length=2)
    filename = models.CharField(max_length=20, blank=True)
    office = models.CharField(max_length=1, blank=True)
    reason = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'tickles'

class Timeb(models.Model):
    timeb1 = models.IntegerField(null=True, blank=True)
    timeb2 = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'timeb'

class Timebank(models.Model):
    tid_no = models.IntegerField(null=True, blank=True)
    tdate = models.DateField(null=True, blank=True)
    tdate1 = models.DateField(null=True, blank=True)
    tdate2 = models.DateField(null=True, blank=True)
    debit = models.IntegerField(null=True, blank=True)
    credit = models.IntegerField(null=True, blank=True)
    tname = models.CharField(max_length=30, blank=True)
    tnote = models.CharField(max_length=80, blank=True)
    ttot = models.IntegerField(null=True, blank=True)
    tdate3 = models.DateField(null=True, blank=True)
    tdate5 = models.DateField(null=True, blank=True)
    tdate6 = models.DateField(null=True, blank=True)
    tcode = models.IntegerField(null=True, blank=True)
    tbinst = models.CharField(max_length=30, blank=True)
    tslip = models.CharField(max_length=8, blank=True)
    truntot = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'timebank'

class Tomtest(models.Model):
    firstname = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, blank=True)
    class Meta:
        db_table = 'tomtest'

class Travel(models.Model):
    traveler = models.CharField(max_length=30, blank=True)
    datereq = models.DateField(null=True, blank=True)
    dest = models.CharField(max_length=20, blank=True)
    departm = models.CharField(max_length=10, blank=True)
    purpose = models.CharField(max_length=20, blank=True)
    case = models.CharField(max_length=20, blank=True)
    fileno = models.CharField(max_length=10, blank=True)
    depdate = models.DateField(null=True, blank=True)
    deptime = models.CharField(max_length=7, blank=True)
    retdate = models.DateField(null=True, blank=True)
    rettime = models.CharField(max_length=7, blank=True)
    plane = models.CharField(max_length=10, blank=True)
    car = models.CharField(max_length=10, blank=True)
    cab = models.CharField(max_length=10, blank=True)
    hotel = models.CharField(max_length=10, blank=True)
    rtbupl = models.CharField(max_length=10, blank=True)
    reqby = models.CharField(max_length=20, blank=True)
    dateby = models.DateField(null=True, blank=True)
    arrange = models.CharField(max_length=10, blank=True)
    ardate = models.DateField(null=True, blank=True)
    agency = models.CharField(max_length=15, blank=True)
    confirm = models.CharField(max_length=10, blank=True)
    fltdt1 = models.DateField(null=True, blank=True)
    from1 = models.CharField(max_length=10, blank=True)
    airline1 = models.CharField(max_length=10, blank=True)
    fltno1 = models.CharField(max_length=5, blank=True)
    depttime1 = models.CharField(max_length=7, blank=True)
    to1 = models.CharField(max_length=10, blank=True)
    arrtime1 = models.CharField(max_length=7, blank=True)
    fltdt2 = models.DateField(null=True, blank=True)
    from2 = models.CharField(max_length=10, blank=True)
    airline2 = models.CharField(max_length=10, blank=True)
    fltno2 = models.CharField(max_length=5, blank=True)
    depttime2 = models.CharField(max_length=7, blank=True)
    to2 = models.CharField(max_length=10, blank=True)
    arrtime2 = models.CharField(max_length=7, blank=True)
    hotel2 = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=13, blank=True)
    secure = models.CharField(max_length=10, blank=True)
    fax = models.CharField(max_length=13, blank=True)
    gfax = models.CharField(max_length=13, blank=True)
    chkin = models.DateField(null=True, blank=True)
    chkout = models.DateField(null=True, blank=True)
    smoke = models.CharField(max_length=1, blank=True)
    nsmoke = models.CharField(max_length=1, blank=True)
    carco = models.CharField(max_length=10, blank=True)
    cartype = models.CharField(max_length=10, blank=True)
    carno = models.CharField(max_length=10, blank=True)
    with_field = models.CharField(max_length=26, db_column='with', blank=True) # Field renamed because it was a Python reserved word.
    comments = models.CharField(max_length=60, blank=True)
    rtb = models.CharField(max_length=5, blank=True)
    upl = models.CharField(max_length=5, blank=True)
    ob = models.CharField(max_length=5, blank=True)
    rtbdt = models.DateField(null=True, blank=True)
    hours = models.CharField(max_length=5, blank=True)
    first = models.CharField(max_length=5, blank=True)
    second = models.CharField(max_length=5, blank=True)
    auth = models.CharField(max_length=20, blank=True)
    authdt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'travel'

class Trticket(models.Model):
    trid_no = models.IntegerField()
    tr_join = models.IntegerField()
    tidate = models.DateField()
    tinote = models.CharField(max_length=150, blank=True)
    fixdate = models.DateField(null=True, blank=True)
    fixnote = models.CharField(max_length=20, blank=True)
    fixtech = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = 'trticket'

class Unitmod(models.Model):
    batesnuma = models.IntegerField()
    batesnumb = models.IntegerField()
    desctype = models.CharField(max_length=55, blank=True)
    class_field = models.CharField(max_length=42, db_column='class', blank=True) # Field renamed because it was a Python reserved word.
    date = models.CharField(max_length=8)
    desckeya = models.CharField(max_length=150, blank=True)
    desclass = models.CharField(max_length=168, blank=True)
    comma = models.CharField(max_length=54, blank=True)
    commb = models.CharField(max_length=54, blank=True)
    class Meta:
        db_table = 'unitmod'

class VMachineList(models.Model):
    mach_name = models.CharField(max_length=15, blank=True)
    fullname = models.TextField(blank=True)
    muser = models.CharField(max_length=3)
    class Meta:
        db_table = 'v_machine_list'

class VMemberelist(models.Model):
    email = models.CharField(max_length=50, blank=True)
    id_no = models.IntegerField()
    minst = models.CharField(max_length=7)
    stat = models.CharField(max_length=3, blank=True)
    rforsup = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'v_memberelist'

class VVoterreport(models.Model):
    voter_id = models.IntegerField()
    voter_join = models.IntegerField()
    iabbr = models.CharField(max_length=7, blank=True)
    voter_desc = models.CharField(max_length=50, blank=True)
    voter_date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'v_voterreport'

class Voter(models.Model):
    affnum = models.CharField(max_length=10, blank=True)
    precinct = models.CharField(max_length=5, blank=True)
    portion = models.CharField(max_length=3, blank=True)
    first = models.CharField(max_length=10, blank=True)
    mid = models.CharField(max_length=10, blank=True)
    last = models.CharField(max_length=20, blank=True)
    sfx = models.CharField(max_length=3, blank=True)
    title = models.CharField(max_length=3, blank=True)
    resaddr = models.CharField(max_length=20, blank=True)
    rescty = models.CharField(max_length=15, blank=True)
    resst = models.CharField(max_length=2, blank=True)
    reszip = models.CharField(max_length=5, blank=True)
    rzipxt = models.CharField(max_length=5, blank=True)
    birthdt = models.CharField(max_length=10, blank=True)
    birthst = models.CharField(max_length=2, blank=True)
    areacode = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=7, blank=True)
    information = models.CharField(max_length=20, blank=True)
    regdate = models.CharField(max_length=10, blank=True)
    pty = models.CharField(max_length=1, blank=True)
    special = models.CharField(max_length=10, blank=True)
    condist = models.CharField(max_length=2, blank=True)
    sendist = models.CharField(max_length=2, blank=True)
    asmdist = models.CharField(max_length=2, blank=True)
    supdist = models.CharField(max_length=2, blank=True)
    ctydist = models.CharField(max_length=2, blank=True)
    batchdate = models.CharField(max_length=10, blank=True)
    maddr1 = models.CharField(max_length=20, blank=True)
    maddr2 = models.CharField(max_length=20, blank=True)
    mcity = models.CharField(max_length=15, blank=True)
    mst = models.CharField(max_length=2, blank=True)
    mzip = models.CharField(max_length=5, blank=True)
    mzipxt = models.CharField(max_length=4, blank=True)
    bday = models.CharField(max_length=10, blank=True)
    class Meta:
        db_table = 'voter'

class VoterCcpoa(models.Model):
    voter_id = models.IntegerField()
    voter_join = models.IntegerField()
    voter_chap = models.SmallIntegerField(null=True, blank=True)
    voter_code = models.CharField(max_length=3, blank=True)
    voter_date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'voter_ccpoa'

class VoterCodes(models.Model):
    voter_id = models.IntegerField()
    voter_code_join = models.CharField(max_length=3, blank=True)
    voter_desc = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'voter_codes'

class Zipcode(models.Model):
    zzip = models.CharField(max_length=10)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2, blank=True)
    zone = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'zipcode'

class ZipcodeOld(models.Model):
    zzip = models.CharField(max_length=10)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2, blank=True)
    zone = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'zipcode_old'

class Zipcounty(models.Model):
    zip = models.IntegerField()
    city = models.TextField()
    county = models.TextField()
    state = models.TextField()
    class Meta:
        db_table = 'zipcounty'

