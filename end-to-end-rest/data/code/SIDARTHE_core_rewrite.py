def SIDARTHE_model(y, t, alpha, beta, gamma, delta, epsilon, mu, zeta, lamb, eta, rho, theta, kappa, nu, xi, sigma, tau):
    S, I, D, A, R, T, H, E = y
    dSdt = -S*alpha*I - S*beta*D - S*gamma*A - S*delta*R
    dIdt = S*alpha*I + S*beta*D + S*gamma*A + S*delta*R - I*epsilon - I*zeta  - I*lamb
    dDdt = epsilon*I - D*eta - D*rho
    dAdt = zeta*I - theta*A - mu*A - kappa*A
    dRdt = eta*D + theta*A - nu*R - xi*R
    dTdt = mu*A + nu*R - sigma*T - tau*T
    dHdt = lamb*I + rho*D + kappa*A + xi*R + sigma*T
    dEdt = tau*T
    
    return dSdt, dIdt, dDdt, dAdt, dRdt, dTdt, dHdt, dEdt