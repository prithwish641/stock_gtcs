from flask import Flask, render_template, redirect,flash, url_for, request, Response
from gtcs_Stock import application, db, bcrypt
from gtcs_Stock.forms import RegistrationForm, LoginForm, NewLogin
from gtcs_Stock.models import User, NewCompany, UnitMaster, ItemMaster
from flask_login import login_user, current_user, logout_user, login_required
import flask_login
import flask_mail
import flask_bcrypt




posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@application.route("/")
@application.route("/home")
def home():
    return render_template('home.html')


@application.route("/about")
def about():
    return render_template('about.html', title='About')


@application.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.username.data, email=form.email.data, password = hashed_password, location=form.location.data, phn_number=form.phn_number.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('loginchoice'))
    return render_template('register.html', title='Register', form=form)


@application.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash("Your password and MailId Does not match")
    return render_template('login.html', title='Login', form=form)

@application.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@application.route("/loginchoice", methods=['GET', 'POST'])
def loginchoice():
    return render_template('login1.html')

@application.route("/loginasnew", methods=['GET', 'POST'])
def loginasnew():
    form = NewLogin()
    if form.validate_on_submit():
        new_company = NewCompany(comp_name=form.comp_name.data, website=form.website.data, regd_address=form.regd_address.data,work_address=form.work_address.data, type_of_business=form.type_of_business.data, pincode=form.pincode.data, email=form.email.data, vat=form.vat.data, tin=form.tin.data, gstin=form.gstin.data, cin=form.cin.data, pan=form.pan.data, service_tax=form.service_tax.data, mfg=form.mfg.data, dl=form.dl.data, telephone=form.telephone.data, fax=form.fax.data)
        db.session.add(new_company)
        db.session.commit()
        flash("Your data is saved")
        return redirect(url_for('loginasnew'))
    return render_template('newlogin.html', form=form)

@application.route("/dashboard")
def dashboard():
    return render_template('index.html')

@application.route("/dashboardv2")
def dashboardv2():
    return render_template('index2.html')

@application.route("/dashboardv3")
def dashboardv3():
    return render_template('index3.html')

@application.route("/master")
def master():
    return render_template('master.html')

@application.route("/unitmaster", methods=['GET', 'POST'])
def unitmaster():
    unit_code = request.form.get("unit_code")
    unit = request.form.get("unit")
    desc = request.form.get("desc")
    if unit is not None:
        unit_master = UnitMaster(unit_code=unit_code, unit=unit, desc=desc)
        db.session.add(unit_master)
        db.session.commit()
        flash(f'successfully Saved')
        return redirect(url_for('dashboard'))
    return render_template('validation.html')

@application.route("/unitmastersearch", methods=['GET', 'POST'])
def unitmastersearch():
    data = UnitMaster.query.all()
    return render_template('item_list_unit_master.html', data=data)

@application.route("/uinitsearch", methods=['GET', 'POST'])
def uinitsearch():
    temp = request.form.get("select_type")
    data = UnitMaster.query.filter_by(unit=temp).first()
    return render_template('item_list_unit_master.html', data=data)

@application.route("/itemmaster")
def itemmaster():
    item_barcode = request.form.get("item_barcode")
    item_name = request.form.get("item_name")
    desc = request.form.get("desc")
    item_model = request.form.get("item_model")
    godown = request.form.get("godown")
    purchase = request.form.get("purchase")
    category = request.form.get("category")
    unit = request.form.get("unit")
    min_stock = request.form.get("min_stock")
    open_stock = request.form.get("open_stock")
    gst = request.form.get("gst")
    hsn = request.form.get("hsn")
    batch = request.form.get("batch")
    mfg = request.form.get("mfg")
    expire = request.form.get("expire")

    if gst is not None:
        item_master = ItemMaster(item_barcode=item_barcode,item_name=item_name,desc=desc,item_model=item_model,godown=godown,purchase=purchase,category=category,unit=unit,min_stock=min_stock,open_stock=open_stock,gst=gst,hsn=hsn,batch=batch,mfg=mfg,expire=expire)
        db.session.add(item_master)
        db.session.commit()
        flash(f'successfully Saved')
        return redirect(url_for('itemmaster'))
    return render_template('Item_Master.html')


@application.route("/itemmastersearch", methods=['GET', 'POST'])
def itemmastersearch():
    data = ItemMaster.query.all()
    return render_template('Item_master_search.html', data=data)


@application.route("/itemcategory")
def itemcategory():
    return render_template('Item_category.html')

@application.route("/ratemaster",  methods=['GET', 'POST'])
def ratemaster():
    return render_template('ratemaster.html')

@application.route("/sales")
def sales():
    return render_template('sales.html')

@application.route("/purchase")
def purchase():
    return render_template('purchase.html')

@application.route("/customers")
def customers():
    return render_template('customers.html')

@application.route("/areamaster")
def areamaster():
    return render_template('area_master.html')