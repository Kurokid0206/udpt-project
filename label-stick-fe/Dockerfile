FROM node:20-alpine3.17 as build-venv

COPY package.json yarn.lock ./
RUN yarn install


FROM node:20-alpine3.17 as build

COPY --from=build-venv /node_modules /node_modules
ENV PATH /node_modules/.bin:$PATH
COPY . /app/label-stick-fe
WORKDIR /app/label-stick-fe
ENTRYPOINT ["yarn", "dev"]
# RUN yarn build


# FROM nginx:1.21.1-alpine as production
# COPY --from=build /app/label-stick-fe/dist /usr/share/nginx/html
# COPY nginx.conf /etc/nginx/nginx.conf
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]
