import { configDefaults, defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
    plugins: [react()],
    test: {
        testDir: './__tests__',
        environment: 'jsdom',
        exclude: [...configDefaults.exclude, 'e2e/*'],
        transformMode: {
            web: [/\.[jt]sx$/],
        },
    },
});
