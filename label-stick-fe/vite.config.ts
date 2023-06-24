import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import { resolve } from "path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],

  resolve: {
    alias: [
      // { find: '@', replacement: resolve(__dirname, '/src') },
      { find: "@views", replacement: resolve(__dirname, "./src/views") },
      {
        find: "@components",
        replacement: resolve(__dirname, "./src/components"),
      },
      { find: "@utils", replacement: resolve(__dirname, "./src/utils") },
      { find: "@layouts", replacement: resolve(__dirname, "./src/layouts") },
      { find: "@routers", replacement: resolve(__dirname, "./src/routers") },
      {
        find: "@apolloClient",
        replacement: resolve(__dirname, "./src/services/apollo"),
      },
    ],
  },
  server: {
    fs: {
      allow: [".."],
    },
  },
});
