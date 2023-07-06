import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

//useState base on userCredential.user from response of firebase
interface UserState {
  userId: number | undefined;
  userName: string | undefined;
  email: string | undefined;
}

//get last session user from localstorage
const getLastSessionLangKey = (): UserState => {
  // Tự lấy data từ local storage hay session ở đây

  //nếu không có dữ liệu phiên đăng nhập trước thì trả về mặc định
  return {
    userId: undefined,
    userName: undefined,
    email: undefined,
  };
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
      console.log(action.payload);
      //sau đó set lại state
      state.email = action.payload.email;
      state.userId = action.payload.userId;
      state.userName = action.payload.userName;
    },
  },
});

export const { setUser } = userSlice.actions;

export default userSlice.reducer;
