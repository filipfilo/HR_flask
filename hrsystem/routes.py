import random
from flask import render_template, url_for, flash, redirect, request
from hrsystem import app, db, bcrypt
from hrsystem.forms import RegistrationForm, LoginForm, AddForm
from hrsystem.models import User, Post, Employee

##############
# ALL ROUTES #
##############


@app.route("/")
@app.route("/employee", methods=['GET', 'POST'])
def homepage():
    employees = Employee.query.all()
    return render_template('allemployees.html', title='All Employees', employees=employees)


@app.route("/findemployee", methods=['GET', 'POST'])
def findemployee():
    return render_template('findemployee.html')


@app.route("/employee/new", methods=['GET', 'POST'])
def addtodb():
    form = AddForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash()
        form.password.data.decode('utf-8')
        randomcislo = str(random.randint(100000, 999999))
        user = Employee(id=form.subsidiary.data + randomcislo, citizenship=form.citizenship.data, city=form.city.data, country_of_residence=form.country_of_residence.data, date_of_birth=form.date_of_birth.data, first_name=form.first_name.data, last_name=form.last_name.data, national_id=form.national_id.data, email=form.email.data, state=form.state.data, street_address=form.street_address.data, telephone_number=form.telephone_number.data, zipcode=form.zipcode.data,
                        password=hashed_password, username=form.username.data, band=form.band.data, contract_beginning=form.contract_beginning.data, contract_end=form.contract_end.data, contract_type=form.contract_type.data, department=form.department.data, employment_status=form.employment_status.data, fte=form.fte.data, salary=form.salary.data, is_manager=form.is_manager.data, job_title=form.job_title.data, manager=form.manager.data, subsidiary=form.subsidiary.data)
        db.session.add(user)
        db.session.commit()

        flash(f"Employee added", 'success')
        return redirect(url_for('homepage'))

    return render_template('addtodb.html', title='Add Employee', form=form, legend='Add Employee')


@app.route("/employee/<string:employee_id>")
def employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    return render_template('employeeid_page.html', title='employee.id', employee=employee)


@app.route("/employee/<string:employee_id>/update", methods=['GET', 'POST'])
def update_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    form = AddForm()
    # TODO
    if form.validate_on_submit():
        employee.subsidiary = form.subsidiary.data
        employee.citizenship = form.citizenship.data
        employee.city = form.city.data
        employee.country_of_residence = form.country_of_residence.data
        employee.date_of_birth = form.date_of_birth.data
        employee.first_name = form.first_name.data
        employee.last_name = form.last_name.data
        employee.national_id = form.national_id.data
        employee.email = form.email.data
        employee.state = form.state.data
        employee.street_address = form.street_address.data
        employee.telephone_number = form.telephone_number.data
        employee.zipcode = form.zipcode.data
        employee.username = form.username.data
        #employee.password = form.password.data
        employee.band = form.band.data
        employee.contract_beginning = form.contract_beginning.data
        employee.contract_end = form.contract_end.data
        employee.contract_type = form.contract_type.data
        employee.department = form.department.data
        employee.employment_status = form.employment_status.data
        employee.fte = form.fte.data
        employee.salary = form.salary.data
        employee.is_manager = form.is_manager.data
        employee.job_title = form.job_title.data
        employee.manager = form.manager.data
        db.session.commit()
        flash("Employee records updated", 'success')

        return redirect(url_for('employee', employee_id=employee.id))
    elif request.method == 'GET':
        form.subsidiary.data = employee.subsidiary
        form.citizenship.data = employee.citizenship
        form.city.data = employee.city
        form.country_of_residence.data = employee.country_of_residence
        form.date_of_birth.data = employee.date_of_birth
        form.first_name.data = employee.first_name
        form.last_name.data = employee.last_name
        form.national_id.data = employee.national_id
        form.email.data = employee.email
        form.state.data = employee.state
        form.street_address.data = employee.street_address
        form.telephone_number.data = employee.telephone_number
        form.zipcode.data = employee.zipcode
        form.username.data = employee.username
        form.password.data = employee.password
        form.band.data = employee.band
        form.contract_beginning.data = employee.contract_beginning
        form.contract_end.data = employee.contract_end
        form.contract_type.data = employee.contract_type
        form.department.data = employee.department
        form.employment_status.data = employee.employment_status
        form.fte.data = employee.fte
        form.salary.data = employee.salary
        form.is_manager.data = employee.is_manager
        form.job_title.data = employee.job_title
        form.manager.data = employee.manager
    # TODO
    return render_template('addtodb.html', title='Update Employee', form=form, legend='Update Employee')


@app.route("/employee/<string:employee_id>/delete", methods=['POST'])
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    flash("Employee deleted", 'info')
    return redirect(url_for('homepage'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        req = request.form.getlist('username')
        print(req)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('homepage'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
