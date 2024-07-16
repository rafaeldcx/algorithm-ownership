import recursos as Rec
import mom as Mom

recursos = Rec.Recursos.get_instance()

def main():
   # print(f"ID da instância de Recursos: {id(recursos)}")
    recursos.criar_recursos_pydriller("../algorithm-ownership/data/data_trampoline.csv")
    
    mom = Mom.Mom()
    mom.calcular_propriedade_mom()
    mom.save("result_trampoline.csv")

if __name__ == "__main__":
    main()