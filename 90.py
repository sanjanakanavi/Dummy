'''pip and PyPI
pip is used to install packages
packages are ntg but pack of modules or subpackages,PyPI :python package index
now in command prompt 
python --version:used to check version of python
python -m pip:used to know the usage of pip
pip install (packagename):to install packages
pip list:will give you list of package already present
pip uninstall (packagename):will uninstall package

to create a package ,right click on project-> new-> python package->enter
like this u can create package inside package in any no of levels
if u have multiple package in mian package the in main code we can import them like
:import mainpackagename.subpackagename.modulename   ,in this way we can import any package and access all data
if u want to call a method of diff package then u can like:
    :mainpackagename.subpackagename.modulename.methoname()
if u want to access class then create an object on that class like:
    :objectname=mainpackagename.subpackagename.modulename.classname()
    
other way is to use from keyword
from packagename import modulename
modulename.method()#here u dont have to write full path name

for multilevel importing we can write like
:from mainpackagename.subpackagename import modulename1,modulename2
modulename.method()#calling method from that

if u want to import specific method from any package and module then:
    from mainpackagename.subpackagename.modulename import methodname
    methodname()#calling that method
    
or u can jusr write: from packagename import * #it will import everything and init module also
inside init module u can override it like:__all__=["module1","module2"]
so all module of that package get imported automatically '''
