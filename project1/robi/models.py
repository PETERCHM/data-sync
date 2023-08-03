from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    supplier = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255)
    tax_included = models.DecimalField(max_digits=10, decimal_places=2)
    buyingprice = models.CharField(max_length=50)
    sellingprice = models.CharField(max_length=50)
    promoprice = models.CharField(max_length=50, blank=True, null=True)
    wholesaleprice = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    reorderevel = models.IntegerField(blank=True, null=True)
    allow_alt_description = models.IntegerField()
    is_serialized = models.IntegerField()
    imgid = models.CharField(max_length=255, blank=True, null=True)
    override_default_tax = models.IntegerField()
    is_service = models.IntegerField()
    deleted = models.IntegerField()
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    dateposted = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    companyid = models.CharField(max_length=100)
    store = models.CharField(max_length=50)
    expdate = models.DateField()
    orderamount = models.CharField(max_length=50)
    taxtype = models.CharField(max_length=30)
    shortname = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    uom = models.CharField(max_length=20)
    producttype = models.CharField(max_length=30)
    assetaccount = models.CharField(max_length=30)
    salesaccount = models.CharField(max_length=30)
    expenseaccount = models.CharField(max_length=30)
    vattype = models.CharField(max_length=20)
    reorderquantity = models.CharField(max_length=20, blank=True, null=True)
    hscode = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Mainmenu(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(unique=True, max_length=255)
    icon = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    url = models.TextField()
    type = models.CharField(max_length=50)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mainmenu'
        

class SalesOrdercancelled(models.Model):
    myinvoice = models.CharField(unique=True, max_length=50, blank=True, null=True)
    invoice = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.CharField(max_length=100)
    salestype = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    dateposted = models.CharField(max_length=50)
    address = models.TextField()
    description = models.TextField()
    user = models.CharField(max_length=50)
    bprice = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    sprice = models.CharField(max_length=100)
    balance = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    mode = models.CharField(max_length=50)
    companyid = models.CharField(max_length=100)
    date = models.DateTimeField()
    maincategory = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=30)
    ordersales = models.CharField(max_length=20)
    uom = models.CharField(max_length=30)
    sales = models.CharField(max_length=30)
    updatedat = models.CharField(max_length=50)
    updatedby = models.CharField(max_length=10)
    taxindicator = models.CharField(max_length=10)
    serial = models.CharField(max_length=50, blank=True, null=True)
    tax2 = models.CharField(max_length=20)
    discountype = models.CharField(max_length=20)
    discountvalue = models.CharField(max_length=20)
    vattype = models.CharField(max_length=20)
    taxable = models.DecimalField(max_digits=10, decimal_places=2)
    uomqty = models.CharField(max_length=30)
    stockbefore = models.CharField(max_length=30)
    stockafter = models.CharField(max_length=30)
    taxtype = models.CharField(max_length=30)
    stock = models.CharField(max_length=20)
    producttype = models.CharField(max_length=30)
    assetaccount = models.CharField(max_length=30)
    salesaccount = models.CharField(max_length=30)
    expenseaccount = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_ordercancelled'


class SalesOrder(models.Model):
    myinvoice = models.CharField(unique=True, max_length=50, blank=True, null=True)
    invoice = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    qty = models.CharField(max_length=10)
    amount = models.CharField(max_length=100)
    salestype = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    dateposted = models.CharField(max_length=50)
    address = models.TextField()
    description = models.TextField()
    user = models.CharField(max_length=50)
    bprice = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    sprice = models.CharField(max_length=100)
    balance = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    mode = models.CharField(max_length=50)
    companyid = models.CharField(max_length=100)
    date = models.DateTimeField()
    maincategory = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=30)
    ordersales = models.CharField(max_length=20)
    uom = models.CharField(max_length=30)
    sales = models.CharField(max_length=30)
    updatedat = models.CharField(max_length=50)
    updatedby = models.CharField(max_length=10)
    taxindicator = models.CharField(max_length=10)
    serial = models.CharField(max_length=50, blank=True, null=True)
    tax2 = models.CharField(max_length=20)
    discountype = models.CharField(max_length=20)
    discountvalue = models.CharField(max_length=20)
    vattype = models.CharField(max_length=20)
    taxable = models.DecimalField(max_digits=10, decimal_places=2)
    uomqty = models.CharField(max_length=30)
    stockbefore = models.CharField(max_length=30)
    stockafter = models.CharField(max_length=30)
    taxtype = models.CharField(max_length=30)
    stock = models.CharField(max_length=20)
    producttype = models.CharField(max_length=30)
    assetaccount = models.CharField(max_length=30)
    salesaccount = models.CharField(max_length=30)
    expenseaccount = models.CharField(max_length=30, blank=True, null=True)
    start = models.CharField(max_length=20)
    close = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'sales_order'


class Openorders(models.Model):
    code = models.CharField(max_length=50)
    description = models.TextField()
    startdate = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    updatedate = models.CharField(max_length=50)
    companyid = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    messageid = models.CharField(max_length=30)
    updatedby = models.IntegerField()
    updateddate = models.CharField(max_length=30)
    closedate = models.TextField()
    receiver = models.TextField()
    millage = models.CharField(max_length=30)
    fuel = models.CharField(max_length=50)
    trips = models.TextField()
    createdate = models.CharField(max_length=30)
    nextfuel = models.CharField(max_length=20)
    previoufueldate = models.CharField(max_length=30)
    previousfuelused = models.CharField(max_length=20)
    adjusted = models.CharField(max_length=20)
    fuellimit = models.CharField(max_length=20)
    fuelrate = models.CharField(max_length=20)
    exactfuel = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'openorders'


class Attendance(models.Model):
    idno = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date = models.DateTimeField()
    timein = models.CharField(max_length=100)
    timeout = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    createddate = models.CharField(max_length=100)
    comment = models.TextField()
    timediffrence = models.CharField(max_length=5)
    device = models.CharField(max_length=30)
    totaltime = models.CharField(max_length=20, blank=True, null=True)
    checkoutime = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance'

class Activityloggs(models.Model):
    userid = models.CharField(max_length=30)
    timedone = models.CharField(max_length=50)
    actiondone = models.TextField()
    ip = models.TextField()
    companyid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'activityloggs'

class SalesOrderkitchen(models.Model):
    myinvoice = models.CharField(unique=True, max_length=50, blank=True, null=True)
    invoice = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.CharField(max_length=100)
    salestype = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    dateposted = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.TextField()
    user = models.CharField(max_length=50)
    bprice = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    sprice = models.CharField(max_length=100)
    balance = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    mode = models.CharField(max_length=50)
    companyid = models.CharField(max_length=100)
    date = models.DateTimeField()
    maincategory = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=30)
    ordersales = models.CharField(max_length=20)
    uom = models.CharField(max_length=30)
    sales = models.CharField(max_length=30)
    updatedat = models.CharField(max_length=50)
    updatedby = models.CharField(max_length=10)
    taxindicator = models.CharField(max_length=10)
    serial = models.CharField(max_length=50, blank=True, null=True)
    tax2 = models.CharField(max_length=20)
    discountype = models.CharField(max_length=20)
    discountvalue = models.CharField(max_length=20)
    vattype = models.CharField(max_length=20)
    taxable = models.CharField(max_length=50)
    uomqty = models.CharField(max_length=30)
    stockbefore = models.CharField(max_length=30)
    stockafter = models.CharField(max_length=30)
    taxtype = models.CharField(max_length=30)
    stock = models.CharField(max_length=20)
    producttype = models.CharField(max_length=30)
    assetaccount = models.CharField(max_length=30)
    salesaccount = models.CharField(max_length=30)
    expenseaccount = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_orderkitchen'


class Orderlist(models.Model):
    type = models.CharField(max_length=30)
    userid = models.CharField(max_length=30)
    exactime = models.CharField(max_length=50)
    batchid = models.CharField(max_length=50)
    itemid = models.CharField(max_length=30)
    invoice = models.CharField(max_length=30)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    companyid = models.IntegerField()
    branchid = models.IntegerField()
    code = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'orderlist'
