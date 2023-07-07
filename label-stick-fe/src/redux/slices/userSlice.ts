import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

//useState base on userCredential.user from response of firebase
interface UserState {
  userId: number | undefined;
  userName: string | undefined;
  email: string | undefined;
  role: string | undefined;
}

//get last session user from localstorage
const getLastSessionLangKey = (): UserState => {
  // Tự lấy data từ local storage hay session ở đây
  let lastUser: UserState = {
    userId: undefined,
    userName: undefined,
    email: undefined,
    role: undefined,
  };
  let stringFromLocal = localStorage.getItem("user");
  if (stringFromLocal) {
    let userFromLocal = JSON.parse(stringFromLocal);
    lastUser.email = userFromLocal?.email;
    lastUser.userName = userFromLocal?.userName;
    lastUser.userId = userFromLocal?.userId;
    lastUser.role = userFromLocal?.role;
  }

  //nếu không có dữ liệu phiên đăng nhập trước thì trả về mặc định
  return lastUser;
};

// Define the initial state using that type
const initialState: UserState = getLastSessionLangKey();

export const userSlice = createSlice({
  name: "userSlice",
  // `createSlice` will infer the state type from the `initialState` argument
  initialState,
  reducers: {
    setUser: (state, action: PayloadAction<UserState>) => {
      //Lưu user vào localstorage hay session ...
      //your code here
      localStorage.setItem("user", JSON.stringify(action.payload));
      //sau đó set lại state
      state.email = action.payload.email;
      state.userId = action.payload.userId;
      state.userName = action.payload.userName;
      state.role = action.payload.role;
    },
    logout: (state) => {
      //Lưu user vào localstorage hay session ...
      //your code here
      localStorage.removeItem("user");
      //sau đó set lại state
      state.email = undefined;
      state.userId = undefined;
      state.userName = undefined;
      state.role = undefined;
    },
  },
});

export const { setUser, logout } = userSlice.actions;

export default userSlice.reducer;
