const NotFound: React.FC = () => {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        width: "100%",
        height: "100vh",
      }}
    >
      <img
        src="https://ih1.redbubble.net/image.1866340271.2956/st,small,507x507-pad,600x600,f8f8f8.jpg"
        alt=""
        style={{
          width: "30%",
        }}
      />
      <h1>404 not found</h1>
    </div>
  );
};
export default NotFound;
