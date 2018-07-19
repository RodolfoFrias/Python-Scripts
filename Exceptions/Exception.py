try:
    x = int(input("Numero1: "))
    y = 1/x
except ZeroDivisionError:
    print("No se puede dividir entre 0 prro")
except ValueError:
    print("Tiene que ser un entero prro")
except:
    print("Hay no mames wey")

#Ca be like this:
#try:
    #something
#except (except1, except2):
    #something
