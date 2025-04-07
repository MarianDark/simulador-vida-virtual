module.exports = {
    webpack: {
      configure: (webpackConfig) => {
        webpackConfig.resolve.fullySpecified = false;
        return webpackConfig;
      },
    },
  };
  