def jacobi_method(A, b, tol=0.005, N_MAX=20):
    """
    Resolve o sistema linear A * x = b utilizando o método iterativo de Jacobi.
    
    Parâmetros:
      A    : matriz dos coeficientes (lista de listas, quadrada);
      b    : vetor dos termos independentes (lista);
      tol  : tolerância para o critério de parada (default 0.005);
      N_MAX: número máximo de iterações (default 20).
    
    Retorna:
      x    : vetor solução aproximada.
    """
    n = len(A)  # número de equações (e incógnitas)
    # Inicializa x0 como vetor zero
    x0 = [0.0 for _ in range(n)]
    k = 0
    while k < N_MAX:
        xk = [0.0 for _ in range(n)]
        # Para cada equação i
        for i in range(n):
            soma = 0.0
            # Soma os termos j != i
            for j in range(n):
                if i != j:
                    soma -= (A[i][j] / A[i][i]) * x0[j]
            # Calcula o novo valor de x para a equação i
            xk[i] = soma + (b[i] / A[i][i])
        # Verifica o critério de convergência: máximo dos erros absolutos
        diff = max(abs(xk[i] - x0[i]) for i in range(n))
        if diff < tol:
            return xk  # Convergiu, retorna a solução
        # Atualiza o vetor x0 para a próxima iteração
        x0 = xk[:]
        k += 1
    # Se atingir o número máximo de iterações, retorna a última aproximação
    return xk