# 0702 PROGRAMACIÓN ORIENTADA A OBJETOS

# Ejercicio 0702 (2 puntos)
#     - Crea una clase llamada Cuenta
#         - que tendrá los siguientes atributos:
#             - titular (que es una persona)
#             - y cantidad (puede tener decimales).
#                 - El titular será obligatorio
#                 - y la cantidad es opcional.
#         - Construye los siguientes métodos para la clase:
#             - Un constructor,
#                 - donde los datos pueden estar vacíos.
#             - Los setters y getters para cada uno de los atributos.
#                 - El atributo no se puede modificar directamente,
#                 - sólo ingresando o retirando dinero.
#             - mostrar():
#                 - Muestra los datos de la cuenta.
#             - ingresar(cantidad):
#                 - se ingresa una cantidad a la cuenta,
#                 - si la cantidad introducida es negativa, no se hará nada.
#             - retirar(cantidad):
#                 - se retira una cantidad a la cuenta.
#                 - La cuenta puede estar en números rojos.


from lab_040701_person_class import Person

class Account:

    _accountHolder: Person
    _accountBalance: float
    _accountOpeningAmount: float

    def __init__( self, accountHolder, accountAmount = 0 ):
        try:
            if not isinstance( accountHolder, Person ) or accountAmount < 0:
                raise AttributeError
            else:
                print( "Account Created for customer", accountHolder.name, "with DNI", accountHolder.dni )
                self._accountHolder = accountHolder
                self._accountBalance = accountAmount
                self._accountOpeningAmount = accountAmount
                # print( "self.accountHolder.name: ", self.accountHolder.name )
                # print( "self.accountBalance: ", self.accountBalance )
                # print( "self.accountOpeningAmount: ", self.accountOpeningAmount )
        except AttributeError:
            print( "\t> EXCEPTION name getter: Attribute \"accountHolder\" or  \"accountAmount\" is a invalid data" )
    # ·························
    def show( self ):
        try:
            return "Account Holder: " + self.accountHolder.name + "\nAccount Balance: " + str( self.accountBalance ) + "\nAccount Opening Amount: " + str( self.accountOpeningAmount )
        except:
            print( "\t> EXCEPTION show() method: One or more Attributes are not defined" )
    # ·························
    def deposit( self, amount ):
        try:
            if amount > 0:
                oldBalance = self._accountBalance
                self._accountBalance += amount
                return "Old Balance: " + "$ {:,}".format( oldBalance ) + "\t\tNew Balance: " + "$ {:,}".format( self.accountBalance ) + "\t\tDeposit Amount: " + "$ {:,}".format( amount )
            else:
                return "Deposit cannot be done"
        except:
            print( "\t> EXCEPTION deposit() method: amount must be greater than 0" )
    # ·························
    def withdraw( self, amount ):
        try:
            if amount > 0 and amount <= self._accountBalance:
                oldBalance = self._accountBalance
                self._accountBalance -= amount
                return "Old Balance: " + "$ {:,}".format( oldBalance ) + "\t\tNew Balance: " + "$ {:,}".format( self.accountBalance ) + "\t\tWithdraw Amount: " + "$ {:,}".format( amount )
            else:
                return "Insufficient funds\tAccount Balance: $ {:,}".format( self._accountBalance ) + "\tRequested Withdraw: " + "$ {:,}".format( amount )
        except:
            print( "\t> EXCEPTION deposit() method: amount must be a valid quantity" )
    # ·························
    @property
    def accountHolder( self ):
        try:
            if not self._accountHolder:
                raise AttributeError
            else:
                return self._accountHolder
        except AttributeError:
            print( "\t> EXCEPTION name getter: Attribute \"accountHolder\" is not defined" )

    @accountHolder.setter
    def accountHolder( self, accountHolder ):
        try:
            if not isinstance( accountHolder, Person ):
                raise AttributeError
            else:
                self._accountHolder = accountHolder
        except AttributeError:
            print( "\t> EXCEPTION name setter: Invalid value for \"accountHolder\" attribute" )
    # ·························
    @property
    def accountBalance( self ):
        return self._accountBalance

    @accountBalance.setter
    def accountBalance( self, accountBalance ):
        try:
            if isinstance( accountBalance, ( float, int, str, list, dict, tuple, bool ) ):
                raise AttributeError
        except:
            print( "\t> EXCEPTION accountBalance setter: accountBalance CANNOT BE SET DIRECTLY" )
    # ·························
    @property
    def accountOpeningAmount( self ):
        try:
            if self._accountOpeningAmount < 0:
                raise AttributeError
            else:
                return self._accountOpeningAmount
        except:
            print( "\t> EXCEPTION name getter: Attribute \"accountOpeningAmount\" is not defined" )

    @accountOpeningAmount.setter
    def accountOpeningAmount( self, accountOpeningAmount ):
        try:
            if isinstance( accountOpeningAmount, ( float, int, str, list, dict, tuple, bool ) ):
                raise AttributeError
        except:
            print( "\t> EXCEPTION accountOpeningAmount setter: accountBalance CANNOT BE SET DIRECTLY" )
    # ·························


# ········································································
# print( "\nCREATING USER" )
# accountCustomer = Person()
# accountCustomer.name = "Jesús"
# accountCustomer.age = 33
# accountCustomer.dni = "JHS137"

# print( "\nCREATING ACCOUNT" )
# account = Account( accountCustomer, 337 )
# account.accountBalance = 10
# account.accountOpeningAmount = 0

# print( "\nDEPOSIT ACCOUNT" )
# print( account.deposit( 0 ) )
# print( account.deposit( 100 ) )

# print( "\nWITHDRAW ACCOUNT" )
# print( account.withdraw( 1000 ) )
# print( account.withdraw( 300 ) )

# print( "\nSHOW ACCOUNT" )
# print( account.show() )
