{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    pkgs.uv
    pkgs.pkg-config
    pkgs.libxml2
  ];
}
