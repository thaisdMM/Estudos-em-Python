from abc import ABC, abstractmethod
from typing import List
from datetime import datetime


class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @abstractmethod
    def exibir_dados(self):
        pass


class Paciente(Pessoa):
    def __init__(self, nome: str, cpf: str, convenio: str):
        super().__init__(nome, cpf)
        self._convenio = convenio

    @property
    def convenio(self):
        return self._convenio

    def exibir_dados(self):
        return f"Paciente: {self.nome} | CPF: {self.cpf} | Convênio: {self.convenio}"


class Medico(Pessoa):
    def __init__(self, nome: str, cpf: str, especialidade: str):
        super().__init__(nome, cpf)
        self._especialidade = especialidade

    @property
    def especialidade(self):
        return self._especialidade

    def exibir_dados(self):
        return f"Médico: {self.nome} | CPF: {self.cpf} | Especialidade: {self.especialidade}"


class Consulta:
    def __init__(self, paciente: Paciente, medico: Medico, data_hora: datetime):
        self._paciente = paciente
        self._medico = medico
        self._data_hora = data_hora

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    @property
    def data_hora(self):
        return self._data_hora

    def exibir_resumo(self):
        return (
            f"Consulta agendada:\n"
            f"Data/Hora: {self.data_hora.strftime('%d/%m/%Y %H:%M')}\n"
            f"{self.paciente.exibir_dados()}\n"
            f"{self.medico.exibir_dados()}"
        )


class AgendaConsultas:
    def __init__(self):
        self._consultas: List[Consulta] = []

    def agendar_consulta(self, consulta: Consulta):
        self._consultas.append(consulta)
        print("Consulta agendada com sucesso!")

    def exibir_consultas(self):
        if not self._consultas:
            print("Nenhuma consulta agendada.")
            return
        for c in self._consultas:
            print("-" * 40)
            print(c.exibir_resumo())


# Simulação de uso do sistema
if __name__ == "__main__":
    paciente1 = Paciente("Ana Silva", "123.456.789-00", "Unimed")
    paciente2 = Paciente("Carlos Souza", "987.654.321-00", "Particular")

    medico1 = Medico("Dr. João", "111.222.333-44", "Cardiologia")
    medico2 = Medico("Dra. Maria", "555.666.777-88", "Dermatologia")

    consulta1 = Consulta(paciente1, medico1, datetime(2025, 8, 5, 14, 30))
    consulta2 = Consulta(paciente2, medico2, datetime(2025, 8, 6, 10, 0))

    agenda = AgendaConsultas()
    agenda.agendar_consulta(consulta1)
    agenda.agendar_consulta(consulta2)

    agenda.exibir_consultas()
