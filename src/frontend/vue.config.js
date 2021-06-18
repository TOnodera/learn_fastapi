module.exports = {
  transpileDependencies: ['vuetify'],
  pages: {
    top: {
      entry: 'src/main.js',
      template: 'public/index.html',
      filename: 'index.html',
    },
    admin: {
      entry: 'src/admin.js',
      template: 'public/admin.html',
      filename: 'admin.html',
    },
  },
};
