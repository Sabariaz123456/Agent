{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNBOs5O5WaOTQwY74a52JdX",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sabariaz123456/Agent/blob/main/Agent.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "8v_B4T70AlDh"
      },
      "outputs": [],
      "source": [
        "# Ye basic Agent class hai\n",
        "class Agent:\n",
        "    def __init__(self, name, instructions, model):\n",
        "        self.name = name\n",
        "        self.instructions = instructions\n",
        "        self.model = model\n",
        "\n",
        "    def run(self, input):\n",
        "        return f\"{self.name} ne handle kiya: '{input}' using {self.model}\"\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Ye Manager class hai jo sub agents ko kaam deta hai\n",
        "class Manager(Agent):\n",
        "    def __init__(self, name, instructions, model, agents):\n",
        "        super().__init__(name, instructions, model)\n",
        "        self.agents = agents\n",
        "\n",
        "    def run(self, input):\n",
        "        print(f\"👨‍💼 Manager ko task mila: {input}\")\n",
        "        results = []\n",
        "        for agent in self.agents:\n",
        "            result = agent.run(input)\n",
        "            print(f\"➡️ Task gaya {agent.name} ko → {result}\")\n",
        "            results.append(result)\n",
        "        return \"\\n\".join(results)\n"
      ],
      "metadata": {
        "id": "_EwWMJwSAzoi"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Ye function system chalayega\n",
        "def Runner_run():\n",
        "    # Agents define karo\n",
        "    web_dev = Agent(\"Web Developer\", \"Website banao\", \"GPT-4\")\n",
        "    mobile_dev = Agent(\"Mobile App Developer\", \"App banao\", \"GPT-4\")\n",
        "    marketing = Agent(\"Marketing Agent\", \"Marketing karo\", \"GPT-4\")\n",
        "\n",
        "    # Manager banao aur agents uske andar daalo\n",
        "    manager = Manager(\n",
        "        name=\"Manager\",\n",
        "        instructions=\"Kaam distribute karo\",\n",
        "        model=\"GPT-4\",\n",
        "        agents=[web_dev, mobile_dev, marketing]\n",
        "    )\n",
        "\n",
        "    # Input dena hai system ko\n",
        "    input_task = \"Build a ecommerce web\"\n",
        "    print(\"🔁 Runner start ho gaya...\")\n",
        "    final_output = manager.run(input_task)\n",
        "    print(\"\\n✅ Final Output:\")\n",
        "    return final_output\n"
      ],
      "metadata": {
        "id": "bk2tunyTA3Su"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "output = Runner_run()\n",
        "print(output)\n"
      ],
      "metadata": {
        "id": "UfpbRoJqA-ZG",
        "outputId": "b3d19c51-48db-4a4a-bc16-1a59688167ff",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🔁 Runner start ho gaya...\n",
            "👨‍💼 Manager ko task mila: Build a ecommerce web\n",
            "➡️ Task gaya Web Developer ko → Web Developer ne handle kiya: 'Build a ecommerce web' using GPT-4\n",
            "➡️ Task gaya Mobile App Developer ko → Mobile App Developer ne handle kiya: 'Build a ecommerce web' using GPT-4\n",
            "➡️ Task gaya Marketing Agent ko → Marketing Agent ne handle kiya: 'Build a ecommerce web' using GPT-4\n",
            "\n",
            "✅ Final Output:\n",
            "Web Developer ne handle kiya: 'Build a ecommerce web' using GPT-4\n",
            "Mobile App Developer ne handle kiya: 'Build a ecommerce web' using GPT-4\n",
            "Marketing Agent ne handle kiya: 'Build a ecommerce web' using GPT-4\n"
          ]
        }
      ]
    }
  ]
}