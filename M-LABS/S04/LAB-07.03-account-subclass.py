# 0703 PROGRAMACIÓN ORIENTADA A OBJETOS

# Ejercicio 0703 (2 puntos)
#     - Vamos a definir ahora una “Cuenta Joven”,
#         - para ello vamos a crear una nueva clase Cuenta Joven
#         - que deriva de la anterior.
#         - Cuando se crea esta nueva clase,
#             - además del titular
#             - y la cantidad
#             - se debe guardar una bonificación que estará expresada en tanto por ciento.
#         - Construye los siguientes métodos para la clase:
#             - Un constructor.
#             - Los setters y getters para el nuevo atributo.

#         - En esta ocasión los titulares de este tipo de cuenta
#             - tienen que ser mayor de edad;
#             - por lo tanto hay que crear un método es TitularVálido()
#                 - que devuelve verdadero si el titular es mayor de edad pero menor de 25 años
#                 - y falso en caso contrario.

#         - Además la retirada de dinero
#             - sólo se podrá hacer si el titular es válido.

#         - El método mostrar()
#             - debe devolver el mensaje de “Cuenta Joven”
#             - y la bonificación de la cuenta.

#         # Piensa los métodos heredados de la clase madre que hay que reescribir.


from lab_040701_person_class import Person
from lab_040702_account_class import Account

class YoungAccount( Account ):

    _accountBonus: float

    def __init__( self, accountHolder, accountAmount = 0, accountBonus = 0 ):
        try:
            if not isinstance( accountHolder.age, int ) or not( accountHolder.age >= 18 and accountHolder.age < 25 ):
                raise AttributeError
            else:
                super().__init__( accountHolder, accountAmount )
                self.accountBonus = accountBonus
        except:
            print( "\t> EXCEPTION name getter: Attribute \"Account Holder Age\" is a invalid data, Account Can't be created" )
    # ·························
    def show( self ):
        try:
            return  "\nYOUNG ACCOUNT\n" + "Account Bonus: " + str( self.accountBonus ) + "\n" + super().show()
        except:
            print( "\t> EXCEPTION show() method: Account Bonus is not defined" )
    # ·························
    def withdraw( self, amount ):
        if self.isHolderValid:
            return super().withdraw( amount )
    # ·························
    @property
    def isHolderValid( self ):
        return True if self.accountHolder.age >= 18 and self.accountHolder.age < 25 else False
    # ·························
    @property
    def accountBonus( self ):
        return self._accountBonus

    @accountBonus.setter
    def accountBonus( self, accountBonus ):
        self._accountBonus = accountBonus
    # ·························


# ········································································
print( "\nCREATING USER" )
person = Person()
person.name = "Pablo"
person.dni = "C1313"
person.age = 18
# If age is >= 18 and < 25, some actions cant be performed
# person.age = 17

print( "\nCREATING YOUNG ACCOUNT" )
youngAccount = YoungAccount( person )
print( youngAccount.show() )

print( "\nIS VALID YOUNG ACCOUNT" )
print( "Valid age: ", youngAccount.isHolderValid )

print( "\nDEPOSIT" )
print( "Valid age: ", youngAccount.deposit( 100.50 ) )

print( "\nWITHDRAW" )
print( "Valid age: ", youngAccount.withdraw( 500 ) )
print( "Valid age: ", youngAccount.withdraw( 100 ) )
