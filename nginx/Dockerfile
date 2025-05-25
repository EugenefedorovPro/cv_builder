# The first stage
# Build React static files

FROM node:24-bullseye AS build

WORKDIR /app
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./
RUN npm ci
COPY ./frontend/ ./
COPY .env /.env
RUN npm run build

# The second stage
# Copy React static files and start nginx
FROM nginx:1.27.5
COPY --from=build /app/build /usr/share/nginx/html
COPY ./nginx/monitor.conf /etc/nginx/conf.d/monitor.conf
COPY ./backend/staticfiles /app/staticfiles
CMD ["nginx", "-g", "daemon off;"]
