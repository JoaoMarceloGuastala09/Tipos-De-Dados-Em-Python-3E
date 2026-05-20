{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMGLq1vyjimcEcq3Wnj3BBo"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vi1D_fJQt8IY",
        "outputId": "efa3717d-ffa6-45c5-ce5b-c8f86628be62"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "idade : \n",
            "17\n",
            "<class 'int'> \n",
            "\n",
            "altura : \n",
            "1.6\n",
            "<class 'float'> \n",
            "\n",
            "nome : \n",
            "Jonas Carvalho\n",
            "<class 'str'> \n",
            "\n",
            "briga : \n",
            "False\n",
            "<class 'bool'> \n",
            "\n",
            "frutas : \n",
            "['bluberry', 'morango', 'manga']\n",
            "<class 'list'> \n",
            "\n",
            "coordenadas : \n",
            "(52.64, 24.325)\n",
            "<class 'tuple'> \n",
            "\n",
            "numeros : \n",
            "{1, 2, 3, 4, 5}\n",
            "<class 'set'> \n",
            "\n",
            "pessoas : \n",
            "{'nome': 'NathIngrid', 'idade': 17}\n",
            "<class 'dict'> \n",
            "\n",
            "valor : \n",
            "None\n",
            "<class 'NoneType'> \n",
            "\n"
          ]
        }
      ],
      "source": [
        "# Tipos de dados no python - revisão\n",
        "\n",
        "#INT\n",
        "idade = 17\n",
        "print(\"idade : \")\n",
        "print(idade)\n",
        "print(type(idade), \"\\n\")\n",
        "\n",
        "#FLOAT (Ponto Flutuante) valores com virgula\n",
        "altura = 1.60\n",
        "print(\"altura : \")\n",
        "print(altura)\n",
        "print(type(altura), \"\\n\")\n",
        "\n",
        "#STR (string) texto\n",
        "nome = \"Jonas Carvalho\"\n",
        "print(\"nome : \")\n",
        "print(nome)\n",
        "print(type(nome), \"\\n\")\n",
        "\n",
        "#BOOL boleano: SIM, NÃO, VERDADE, MENTIRA, LIGADO, DESIGADO\n",
        "briga = False\n",
        "print(\"briga : \")\n",
        "print(briga)\n",
        "print(type(briga), \"\\n\")\n",
        "\n",
        "#List Lista (Coleção Ordenada)\n",
        "frutas = [\"bluberry\", \"morango\", \"manga\"]\n",
        "print(\"frutas : \")\n",
        "print(frutas)\n",
        "print(type(frutas), \"\\n\")\n",
        "\n",
        "#Tuple Tuplas Duplas, como por exemplo, coordenadas\n",
        "coordenadas = (52.640, 24.325)\n",
        "print(\"coordenadas : \")\n",
        "print(coordenadas)\n",
        "print(type(coordenadas), \"\\n\")\n",
        "\n",
        "#Set - Conjunto\n",
        "numeros = {1, 2, 3, 3, 4, 5, 5, 5}\n",
        "print(\"numeros : \")\n",
        "print(numeros)\n",
        "print(type(numeros), \"\\n\")\n",
        "\n",
        "#Dict - Dicionario\n",
        "pessoas = {\"nome\" : \"NathIngrid\", \"idade\" : 17}\n",
        "print(\"pessoas : \")\n",
        "print(pessoas)\n",
        "print(type(pessoas), \"\\n\")\n",
        "\n",
        "#None Type - quanod não tem nada, mas é preciso informar um valor\n",
        "valor = None\n",
        "print(\"valor : \")\n",
        "print(valor)\n",
        "print(type(valor), \"\\n\")\n",
        "\n"
      ]
    }
  ]
}