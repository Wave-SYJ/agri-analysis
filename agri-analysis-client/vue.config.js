module.exports = {
  devServer: {
    host: 'localhost',
    port: 8080,
    proxy: {
        '/api': {
            target: 'http://localhost:5000',
            changeOrigin: true,
            ws: true,
            pathRewrite: {
              '^/api': ''
            }
        }
    }
  }
}