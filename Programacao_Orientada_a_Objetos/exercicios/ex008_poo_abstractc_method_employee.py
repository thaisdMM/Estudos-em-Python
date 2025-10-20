# ======================================================================================================================
# ENUNCIADO RESUMIDO (EXERCÍCIO 4: ABSTRAÇÃO, COMPOSIÇÃO E MÉTODOS DE CLASSE)
#
# OBJETIVO: Criar um sistema de Funcionários (baseados em Abstração) e Departamentos (utilizando Composição).
#
# 1. CLASSE BASE ABSTRATA (FuncionarioBase): Deve ter construtor (nome, salario) e dois métodos abstratos:
#    - calcular_bonus()
#    - exibir_cargo()
#
# 2. CLASSES CONCRETAS (Gerente, Desenvolvedor): Herdar de FuncionarioBase e implementar os métodos obrigatórios:
#    - Gerente: Bônus de 15%.
#    - Desenvolvedor: Bônus de 10%.
#
# 3. CLASSE DE COMPOSIÇÃO (Department):
#    - Atributo de Instância: _employees (lista) para armazenar objetos Funcionário.
#    - Método de Instância: add_employee() para adicionar um funcionário à lista.
#    - Método de Instância: show_salary() para exibir a folha salarial.
#    - Método de Classe (@classmethod): create_default_department(cls, department_name: str) para criar e retornar
#      uma nova instância de Department pré-populada com 1 Gerente e 2 Desenvolvedores.
#
# ======================================================================================================================

from abc import ABC, abstractmethod # Módulos para implementar a Classe Base Abstrata
from typing import List             # Boa Prática: Type Hinting para listas genéricas


class Employee_base(ABC):
    # Boa Prática: O uso de 'ABC' e '@abstractmethod' garante que as classes filhas
    # implementem os métodos essenciais, forçando o contrato da Abstração.
    def __init__(self, name: str, salary: float):
        super().__init__()
        # Boa Prática: Uso do underline simples (_) para indicar atributos protegidos
        self._name = name
        self._salary = salary

    @abstractmethod
    def calculate_bonus(self):
        # Método Abstrato: Obriga as classes filhas a definir o cálculo específico.
        pass

    @abstractmethod
    def display_employee_position(self):
        # Método Abstrato: Obriga as classes filhas a definir o cargo.
        pass


class Manager(Employee_base):
    def __init__(self, name: str, salary: float):
        # Herança: Chama o construtor da classe base para inicializar nome e salário.
        super().__init__(name, salary)

    def calculate_bonus(self) -> float:
        # Implementação Concreta: Bônus específico para Gerente.
        return self._salary * 0.15

    def display_employee_position(self) -> str:
        # Implementação Concreta: Exibe o cargo.
        return f"The {self._name} position in the company is: Manager."

    def total_salary(self) -> float:
        # Método de Instância: Calcula o salário total usando o bônus implementado.
        return (self.calculate_bonus()) + self._salary


class Developer(Employee_base):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary)

    def calculate_bonus(self) -> float:
        # Implementação Concreta: Bônus específico para Desenvolvedor.
        return self._salary * 0.10

    def display_employee_position(self) -> str:
        return f"The {self._name} position in the company is: Developer."

    def total_salary(self) -> float:
        return (self.calculate_bonus()) + self._salary


class Department:
    def __init__(self):
        # Composição: Atributo de Instância (_employees) armazena objetos Funcionário.
        # Cada instância de Department tem sua própria lista de funcionários (Composição).
        self._employees: List[Employee_base] = []

    # Método de Instância: Opera no estado (_employees) do objeto Department.
    def add_employee(self, employee: Employee_base):
        self._employees.append(employee) # O append() modifica 'in-place' e retorna None (comportamento desejado).

    # Método de Instância: Exibe a folha salarial da lista interna.
    def show_salary(self):
        if not self._employees:
            print("There is no employee for show.")
            return # Boa Prática: Retorno antecipado para listas vazias.

        print("-" * 50)
        for employee in self._employees:
            # Polimorfismo: employee.calculate_bonus() chama o método da classe concreta (Manager ou Developer)
            print(
                f"Employee: {employee._name} | Position: {type(employee).__name__} | Salary: U${employee._salary} | Salary Bonus: U${employee.calculate_bonus():.2f} | Total salary: U${employee.total_salary():.2f}"
            )
        print("-" * 50)

    # Método de Classe (@classmethod): Construtor Alternativo (Factory Method).
    @classmethod
    def create_default_department(cls, department_name: str):
        # 1. Cria a nova instância do Department (cls() chama o __init__).
        new_department = cls()

        # 2. Cria os objetos de funcionários.
        manager = Manager("Luiza", 6500)
        developer1 = Developer("Tiago", 4100)
        developer2 = Developer("Nanda", 4500)

        # 3. Adiciona os funcionários à nova instância (Composição).
        new_department.add_employee(manager)
        new_department.add_employee(developer1)
        new_department.add_employee(developer2)

        # 4. Retorna a instância pré-populada.
        return new_department


# ======================================================================================================================
# EXEMPLOS DE USO
# ======================================================================================================================

# Teste com instâncias individuais (Manager)
alessandra = Manager("Alessandra", 6500)
print("\n--- Teste Alessandra ---")
print(f"Bonus: {alessandra.calculate_bonus():.2f}")
print(alessandra.display_employee_position())
print(f"Total salary: {alessandra.total_salary():.2f}")

# Teste com instâncias individuais (Developer)
leandro = Developer("Leandro", 5000)
print("\n--- Teste Leandro ---")
print(leandro.display_employee_position())
print(f"Total salary: {leandro.total_salary():.2f}")


# ----------------------------------------------------------------------------------------------------------------------
# Demonstração de método de instância (adicionar manualmente)
# ----------------------------------------------------------------------------------------------------------------------
employees_list_manual = Department()
employees_list_manual.add_employee(alessandra)
employees_list_manual.show_salary()


# ----------------------------------------------------------------------------------------------------------------------
# Demonstração do Método de Classe (@classmethod) - Construtor Alternativo
# ----------------------------------------------------------------------------------------------------------------------

# Chamada Correta: Armazena o objeto retornado pelo @classmethod.
tech_consult = Department.create_default_department("Tech Consult")
print("\n--- Folha Salarial - Departamento Padrão (Criado com @classmethod) ---")
tech_consult.show_salary()


# O método de classe é chamado na CLASSE (Department.create_default_department).
# O objeto é retornado e armazenado em 'tech_consult'.
# O objeto 'tech_consult' é quem chama o método de instância 'show_salary()'.