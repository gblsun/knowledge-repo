defmodule Chat do
  def iniciar do
    entradas = ["oi", "teste", "erro grande aqui", "ok", "/count", "/clear", "ola", "sair"]
    loop([], entradas)
  end

  # Implementado - Loop principal recursivo
  def loop(_, []), do: IO.puts("Fim")

  def loop(mensagens, [entrada | resto]) do
    IO.puts("\nEntrada: #{entrada}")
    processar(entrada, mensagens, resto)
  end

  # Implementado - Processamento de entrada separado
  def processar("sair", _mensagens, _resto) do
    IO.puts("Encerrando...")
  end

  def processar("/clear", _mensagens, resto) do
    IO.puts("Mensagens limpas")
    loop([], resto)
  end

  def processar("/count", mensagens, resto) do
    IO.puts("Quantidade: #{length(mensagens)}")
    mostrar(mensagens)
    loop(mensagens, resto)
  end

  def processar(entrada, mensagens, resto) do
    if valida?(entrada) do
      novas = adicionar(mensagens, entrada)
      mostrar(novas)
      loop(novas, resto)
    else
      IO.puts("Mensagem inválida")
      loop(mensagens, resto)
    end
  end

  # Implementado - Função pura de adição
  def adicionar(mensagens, msg), do: mensagens ++ [msg]

  # Implementado - Validação de mensagem
  def valida?(msg) do
    msg != "" and String.length(msg) <= 10
  end

  # Implementado - Recursão para exibir mensagens
  def mostrar([]), do: :ok

  def mostrar([h | t]) do
    IO.puts(h)
    mostrar(t)
  end
end

Chat.iniciar()
