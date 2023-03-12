# Backend (which serves frontend) dockerfile
FROM rust:1.68

WORKDIR /

COPY rust_ws/backend backend

WORKDIR /backend

RUN cargo build --release

COPY index.html /index.html

EXPOSE 80
ENTRYPOINT ["/backend/target/release/backend"]