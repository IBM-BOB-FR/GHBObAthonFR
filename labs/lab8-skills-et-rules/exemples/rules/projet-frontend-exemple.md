# Règles du Projet - Application React TypeScript

## 📋 Vue d'Ensemble

Application web moderne de e-commerce construite avec React, TypeScript et les meilleures pratiques du développement frontend.

## 🏗️ Stack Technique

- **Framework** : React 18+
- **Langage** : TypeScript 5+
- **Build Tool** : Vite
- **State Management** : Zustand
- **Routing** : React Router v6
- **Styling** : Tailwind CSS + CSS Modules
- **Forms** : React Hook Form + Zod
- **API Client** : Axios + React Query
- **Tests** : Vitest + React Testing Library
- **E2E Tests** : Playwright

## 📁 Structure du Projet

```
src/
├── components/          # Composants réutilisables
│   ├── ui/             # Composants UI de base (Button, Input, etc.)
│   ├── layout/         # Composants de layout (Header, Footer, etc.)
│   └── features/       # Composants métier
├── pages/              # Pages de l'application
├── hooks/              # Custom hooks
├── stores/             # State management (Zustand)
├── services/           # Services API
├── utils/              # Fonctions utilitaires
├── types/              # Types TypeScript
├── constants/          # Constantes
└── tests/              # Tests
```

## 💻 Conventions TypeScript

### Types et Interfaces

- **Interfaces** pour les objets et les props de composants
- **Types** pour les unions, intersections et types complexes
- Préfixer les interfaces avec `I` uniquement si nécessaire pour éviter les conflits
- Utiliser `type` pour les props de composants

```typescript
// ✅ Bon
interface User {
  id: string;
  name: string;
  email: string;
}

type UserProps = {
  user: User;
  onEdit: (user: User) => void;
};

// ❌ Éviter
interface IUser { ... }  // Pas de préfixe I sauf si nécessaire
```

### Strict Mode

- TypeScript en mode strict activé
- Pas de `any` (utiliser `unknown` si nécessaire)
- Typer explicitement les retours de fonctions
- Utiliser `as const` pour les constantes

```typescript
// ✅ Bon
const ROLES = ['admin', 'user', 'guest'] as const;
type Role = typeof ROLES[number];

// ❌ Éviter
const ROLES = ['admin', 'user', 'guest'];  // Type trop large
```

## ⚛️ Conventions React

### Composants

- **Functional Components** uniquement (pas de class components)
- **Named exports** pour les composants
- Un composant par fichier
- Nom du fichier = nom du composant (PascalCase)

```typescript
// ✅ Bon - UserCard.tsx
export function UserCard({ user }: UserCardProps) {
  return <div>{user.name}</div>;
}

// ❌ Éviter
export default function UserCard() { ... }  // Pas de default export
```

### Props

- Toujours typer les props
- Destructurer les props dans les paramètres
- Utiliser des valeurs par défaut quand approprié
- Documenter les props complexes

```typescript
type ButtonProps = {
  /** Le texte du bouton */
  label: string;
  /** Variante visuelle du bouton */
  variant?: 'primary' | 'secondary';
  /** Callback au clic */
  onClick: () => void;
  /** Si le bouton est désactivé */
  disabled?: boolean;
};

export function Button({ 
  label, 
  variant = 'primary', 
  onClick, 
  disabled = false 
}: ButtonProps) {
  // ...
}
```

### Hooks

- Préfixer les custom hooks avec `use`
- Un hook par fichier
- Retourner un objet pour les hooks complexes
- Documenter les hooks réutilisables

```typescript
// ✅ Bon - useUser.ts
export function useUser(userId: string) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  // ... logique

  return { user, loading, error };
}
```

### State Management

- Utiliser `useState` pour l'état local
- Utiliser Zustand pour l'état global
- Éviter la prop drilling (utiliser le contexte ou Zustand)
- Garder l'état au plus proche de son utilisation

```typescript
// ✅ Bon - stores/userStore.ts
import { create } from 'zustand';

interface UserState {
  user: User | null;
  setUser: (user: User) => void;
  logout: () => void;
}

export const useUserStore = create<UserState>((set) => ({
  user: null,
  setUser: (user) => set({ user }),
  logout: () => set({ user: null }),
}));
```

## 🎨 Styling

### Tailwind CSS

- Utiliser Tailwind pour la majorité du styling
- Créer des composants réutilisables pour les patterns communs
- Utiliser `clsx` ou `cn` pour les classes conditionnelles

```typescript
import { clsx } from 'clsx';

export function Button({ variant, className, ...props }: ButtonProps) {
  return (
    <button
      className={clsx(
        'px-4 py-2 rounded font-medium',
        variant === 'primary' && 'bg-blue-500 text-white',
        variant === 'secondary' && 'bg-gray-200 text-gray-800',
        className
      )}
      {...props}
    />
  );
}
```

### CSS Modules

- Utiliser pour les styles complexes ou spécifiques
- Nommer les fichiers : `Component.module.css`
- Utiliser camelCase pour les noms de classes

```css
/* Button.module.css */
.button {
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
}

.buttonPrimary {
  background-color: blue;
  color: white;
}
```

## 🔌 API et Data Fetching

### React Query

- Utiliser React Query pour toutes les requêtes API
- Préfixer les query keys avec le domaine : `['users', userId]`
- Gérer les états loading, error et success
- Utiliser les mutations pour les modifications

```typescript
// ✅ Bon - hooks/useUser.ts
export function useUser(userId: string) {
  return useQuery({
    queryKey: ['users', userId],
    queryFn: () => userService.getById(userId),
    staleTime: 5 * 60 * 1000, // 5 minutes
  });
}

export function useUpdateUser() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: userService.update,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['users', data.id] });
    },
  });
}
```

### Services API

- Centraliser les appels API dans des services
- Un service par domaine métier
- Typer les requêtes et réponses

```typescript
// ✅ Bon - services/userService.ts
import axios from './axios';

export const userService = {
  getById: async (id: string): Promise<User> => {
    const { data } = await axios.get<User>(`/users/${id}`);
    return data;
  },

  update: async (user: Partial<User>): Promise<User> => {
    const { data } = await axios.put<User>(`/users/${user.id}`, user);
    return data;
  },
};
```

## 📝 Forms

### React Hook Form + Zod

- Utiliser React Hook Form pour tous les formulaires
- Valider avec Zod
- Typer les données du formulaire

```typescript
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const userSchema = z.object({
  name: z.string().min(2, 'Le nom doit contenir au moins 2 caractères'),
  email: z.string().email('Email invalide'),
  age: z.number().min(18, 'Vous devez avoir au moins 18 ans'),
});

type UserFormData = z.infer<typeof userSchema>;

export function UserForm() {
  const { register, handleSubmit, formState: { errors } } = useForm<UserFormData>({
    resolver: zodResolver(userSchema),
  });

  const onSubmit = (data: UserFormData) => {
    // ...
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* ... */}
    </form>
  );
}
```

## 🧪 Tests

### Tests Unitaires (Vitest)

- Tester la logique métier et les hooks
- Un fichier de test par fichier : `utils.test.ts`
- Nommer les tests : `should ... when ...`

```typescript
// ✅ Bon - utils.test.ts
import { describe, it, expect } from 'vitest';
import { formatPrice } from './utils';

describe('formatPrice', () => {
  it('should format price with 2 decimals', () => {
    expect(formatPrice(10)).toBe('10.00 €');
  });

  it('should handle zero', () => {
    expect(formatPrice(0)).toBe('0.00 €');
  });
});
```

### Tests de Composants (React Testing Library)

- Tester le comportement, pas l'implémentation
- Utiliser les queries par ordre de priorité : getByRole > getByLabelText > getByText
- Simuler les interactions utilisateur

```typescript
// ✅ Bon - Button.test.tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Button } from './Button';

describe('Button', () => {
  it('should call onClick when clicked', async () => {
    const onClick = vi.fn();
    render(<Button label="Click me" onClick={onClick} />);
    
    const button = screen.getByRole('button', { name: /click me/i });
    await userEvent.click(button);
    
    expect(onClick).toHaveBeenCalledTimes(1);
  });
});
```

## 🔒 Sécurité

### Authentification

- Stocker les tokens dans httpOnly cookies (pas localStorage)
- Implémenter le refresh token
- Rediriger vers login si non authentifié

### XSS Protection

- Ne JAMAIS utiliser `dangerouslySetInnerHTML` sans sanitization
- Valider et échapper les entrées utilisateur
- Utiliser DOMPurify si nécessaire

### CSRF Protection

- Utiliser des tokens CSRF pour les mutations
- Vérifier l'origine des requêtes

## ⚡ Performance

### Optimisations React

- Utiliser `React.memo` pour les composants coûteux
- Utiliser `useMemo` et `useCallback` judicieusement
- Lazy load les routes et composants lourds
- Virtualiser les longues listes

```typescript
// ✅ Bon - Lazy loading
import { lazy, Suspense } from 'react';

const Dashboard = lazy(() => import('./pages/Dashboard'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <Dashboard />
    </Suspense>
  );
}
```

### Bundle Size

- Analyser le bundle avec `vite-bundle-visualizer`
- Lazy load les dépendances lourdes
- Tree-shake les imports

```typescript
// ✅ Bon
import { debounce } from 'lodash-es';

// ❌ Éviter
import _ from 'lodash';  // Importe tout lodash
```

## ❌ Ce qu'il faut ÉVITER

- ❌ `any` en TypeScript
- ❌ Default exports
- ❌ Class components
- ❌ Prop drilling excessif
- ❌ State global pour tout
- ❌ Mutations directes du state
- ❌ `useEffect` pour tout (préférer React Query)
- ❌ Inline styles (utiliser Tailwind ou CSS Modules)
- ❌ Console.log en production
- ❌ Secrets dans le code frontend

## ✅ Checklist Avant Commit

- [ ] Code formaté (Prettier)
- [ ] Pas d'erreurs TypeScript
- [ ] Pas d'erreurs ESLint
- [ ] Tests passent
- [ ] Pas de console.log
- [ ] Composants documentés
- [ ] Accessibilité vérifiée (a11y)

## 📚 Ressources

- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [React Query Documentation](https://tanstack.com/query/latest)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)