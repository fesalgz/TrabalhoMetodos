def gauss_seidel(A, b, x0, tol=0.005, N_MAX=200):
    """
    Resolve o sistema linear A * x = b utilizando o método iterativo de Gauss–Seidel.
    
    Parâmetros:
      A    : matriz dos coeficientes (lista de listas, quadrada);
      b    : vetor dos termos independentes (lista);
      x0   : vetor inicial (lista);
      tol  : tolerância para o critério de parada (default 0.005);
      N_MAX: número máximo de iterações (default 200).
      
    Retorna:
      x    : vetor solução aproximada.
    """
    n = len(A)
    k = 0
    while k < N_MAX:
        xk = [0.0] * n
        for i in range(n):
            soma = 0.0
            # Usa os valores já atualizados para j < i
            for j in range(0, i):
                soma += A[i][j] * xk[j]
            # Usa os valores da iteração anterior para j > i
            for j in range(i+1, n):
                soma += A[i][j] * x0[j]
            xk[i] = (b[i] - soma) / A[i][i]
        # Critério de parada: máximo da diferença entre iterações
        diff = max(abs(xk[i] - x0[i]) for i in range(n))
        if diff < tol:
            return xk
        x0 = xk[:]
        k += 1
    return xk